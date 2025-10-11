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

        self.description = f"""# System Agent: This agent is used to perform system related tasks.
        ## Abilities:
        {"\n- ".join([tool.name for tool in self.tools])}
        """

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
