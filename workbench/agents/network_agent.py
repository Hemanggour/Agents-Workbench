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

        self.description = f"""# Network Agent: This agent is used to perform internet related tasks.
        ## Abilities:
        {"\n- ".join([tool.name for tool in self.tools])}
        """  # noqa

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
