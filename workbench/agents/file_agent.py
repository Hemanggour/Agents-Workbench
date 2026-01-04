from typing import Any

from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.file_manager import FileManager
from workbench.utils.prompts import FILE_AGENT_PROMPT


class FileAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = FileManager.get_tools()

        self.agent = create_react_agent(
            name="file_agent",
            model=self.llm,
            tools=self.tools,
            prompt=FILE_AGENT_PROMPT,
        )

        self.description = f"""# File Agent: This agent is used to perform file related tasks.
        ## Abilities:
        {"\n- ".join([tool.name for tool in self.tools])}
        """  # noqa

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]
        return self.agent.invoke({"messages": messages})
