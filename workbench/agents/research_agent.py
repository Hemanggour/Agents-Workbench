from typing import Any

from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.web_manager import WebManager
from workbench.utils.prompts import RESEARCH_AGENT_PROMPT


class ResearchAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = WebManager.get_tools()

        self.agent = create_react_agent(
            name="research_agent",
            model=self.llm,
            tools=self.tools,
            prompt=RESEARCH_AGENT_PROMPT,
        )

        self.description = f"""
# Agent Name: Research Agent

## Role
Handles all research related tasks.

## Allowed Capabilities
This agent can ONLY perform actions using the following tools:
- {"\n- ".join([tool.name for tool in self.tools])}

## Restrictions
- This agent must not perform tasks outside the listed tools.
"""  # noqa

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
