from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.web_tools import WebTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class WebManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = WebTools()

        return [
            tools.duckduckgo_search_tool,
            tools.scrape_url_tool,
            tools.extract_links_tool,
        ]
