import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from langchain_core.tools import StructuredTool

from workbench.utils.config.settings import settings


class WebTools:
    def __init__(self) -> None:
        self.duckduckgo_search_tool = StructuredTool.from_function(
            name="duckduckgo_search",
            func=self.duckduckgo_search,
            args_schema={
                "query": {"type": "string", "description": "Search query"},
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "range": "1-20",
                },
                "search_type": {
                    "type": "string",
                    "description": "Type of search (text, images, videos, news)",
                },
            },
            description="""Search the web using DuckDuckGo.
            You have to make a better query to get better results.
            You can search for text, images, videos, or news.
            Example:
            {
                "query": "search terms",
                "max_results": 5,
                "search_type": "text" | "images" | "videos" | "news"
            }""",
        )

        self.scrape_url_tool = StructuredTool.from_function(
            name="scrape_url",
            func=self.scrape_url,
            args_schema={
                "url": {
                    "type": "string",
                    "description": "The URL to scrape content from",
                }
            },
            description="""Scrape content from a URL.
                Example:
                {
                    "url": "https://example.com"
                }""",
        )

        self.extract_links_tool = StructuredTool.from_function(
            name="extract_links",
            func=self.extract_links,
            args_schema={
                "url": {
                    "type": "string",
                    "description": "The URL to extract links from",
                }
            },
            description="""Extract all links from a webpage.
                Example:
                {
                    "url": "https://example.com"
                }""",
        )

    def scrape_url(self, url: str) -> str:
        """Scrape content from a URL.

        Args:
            url: The URL to scrape content from

        Returns:
            str: The scraped content or an error message
        """
        """Scrape content from a URL"""
        try:
            headers = {"User-Agent": settings.WEB_USER_AGENT}
            response = requests.get(
                url, headers=headers, timeout=settings.WEB_REQUEST_TIMEOUT
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            for script in soup(["script", "style"]):
                script.decompose()

            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = " ".join(chunk for chunk in chunks if chunk)

            if len(text) > settings.WEB_CONTENT_LIMIT:
                text = text[: settings.WEB_CONTENT_LIMIT] + "...\n[Content truncated]"

            return f"Successfully scraped '{url}':\n{text}"
        except requests.RequestException as e:
            return f"Error scraping URL '{url}': {str(e)}"
        except Exception as e:
            return f"Error processing content from '{url}': {str(e)}"

    def extract_links(self, url: str) -> str:
        """Extract all links from a webpage.

        Args:
            url: The URL to extract links from

        Returns:
            str: A formatted string containing the links or an error message
        """
        """Extract all links from a webpage"""
        try:
            headers = {"User-Agent": settings.WEB_USER_AGENT}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            links = []

            for link in soup.find_all("a", href=True):
                href = link["href"]
                text = link.text.strip()
                if href.startswith("http") or href.startswith("//"):
                    links.append(f"{text}: {href}")

            if links:
                return f"Links found on '{url}':\n" + "\n".join(
                    links[: settings.WEB_LINKS_LIMIT]
                )
            else:
                return f"No links found on '{url}'"
        except Exception as e:
            return f"Error extracting links from '{url}': {str(e)}"

    def duckduckgo_search(
        self,
        query: str,
        max_results: int = settings.WEB_SEARCH_MAX_RESULTS,
        search_type: str = settings.WEB_SEARCH_TYPE,
    ) -> str:
        try:
            max_results = max(1, min(int(max_results), 20))  # 1 - 20
            with DDGS() as ddgs:
                search_type = search_type.lower()
                if search_type == "images":
                    results = list(ddgs.images(query, max_results=max_results))
                    return "\n".join(
                        [f"{i+1}. {r['image']}" for i, r in enumerate(results)]
                    )

                elif search_type == "videos":
                    results = list(ddgs.videos(query, max_results=max_results))
                    return "\n".join(
                        [
                            f"{i+1}. {r['title']}\n{r['url']}"
                            for i, r in enumerate(results)
                        ]
                    )

                elif search_type == "news":
                    results = list(ddgs.news(query, max_results=max_results))
                    return "\n".join(
                        [
                            f"{i+1}. {r['title']}\n{r['url']}"
                            for i, r in enumerate(results)
                        ]
                    )

                else:
                    results = list(ddgs.text(query, max_results=max_results))
                    return "\n".join(
                        [
                            f"{i+1}. {r.get('title', 'No title')}\n{r.get('href', '#')}\n{r.get('body', 'No description')}"  # noqa
                            for i, r in enumerate(results)
                        ]
                    )
        except Exception as e:
            return f"Error performing search: {str(e)}"
