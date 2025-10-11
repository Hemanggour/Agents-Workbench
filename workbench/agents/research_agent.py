from typing import Any

from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.web_manager import WebManager
from workbench.utils.prompts import RESEARCH_PROMPT


class ResearchAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = WebManager.get_tools()

        self.agent = create_react_agent(
            name="research_agent",
            model=self.llm,
            tools=self.tools,
            prompt=RESEARCH_PROMPT,
        )

        self.description = f"""# Research Agent: This agent is used to get the results from web.
        ## Abilities:
        {"\n- ".join([tool.name for tool in self.tools])}
        """

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
