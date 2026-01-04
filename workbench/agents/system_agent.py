from typing import Any

from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.system_manager import SystemManager
from workbench.utils.prompts import SYSTEM_AGENT_PROMPT


class SystemAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = SystemManager.get_tools()

        self.agent = create_react_agent(
            name="system_agent",
            model=self.llm,
            tools=self.tools,
            prompt=SYSTEM_AGENT_PROMPT,
        )

        self.description = f"""
# Agent Name: System Agent

## Role
Handles all system related tasks.

## Allowed Capabilities
This agent can ONLY perform actions using the following tools:
- {"\n- ".join([tool.name for tool in self.tools])}

## Restrictions
- This agent must not perform tasks outside the listed tools.
"""  # noqa

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
