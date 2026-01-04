from typing import Any

from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.network_manager import NetworkManager
from workbench.utils.prompts import NETWORK_AGENT_PROMPT


class NetworkAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = NetworkManager.get_tools()

        self.agent = create_react_agent(
            name="network_agent",
            model=self.llm,
            tools=self.tools,
            prompt=NETWORK_AGENT_PROMPT,
        )

        self.description = f"""
# Agent Name: Network Agent

## Role
Handles all network and download related tasks.

## Allowed Capabilities
This agent can ONLY perform actions using the following tools:
- {"\n- ".join([tool.name for tool in self.tools])}

## Restrictions
- This agent must not perform tasks outside the listed tools.
"""  # noqa

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
