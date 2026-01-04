from typing import Any

from langgraph_supervisor import create_supervisor

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.prompts import SUPERVISOR_AGENT_PROMPT


class SupervisorAgent(BaseAgent):
    def __init__(
        self,
        model: str = None,
        model_provider: str = None,
        sub_agents_list: list[BaseAgent] = [],
    ) -> None:
        super().__init__(model, model_provider)

        self.agents_list = sub_agents_list

        self.agent = create_supervisor(
            name="supervisor",
            model=self.llm,
            agents=[agent.agent for agent in self.agents_list],
            prompt=self.__prompt_builder(self.agents_list),
        ).compile()

    def __prompt_builder(self, agents: list[BaseAgent]) -> str:
        prompts = "\n".join(
            [f"{agent.agent.name}: {agent.description}\n" for agent in agents]
        )

        return SUPERVISOR_AGENT_PROMPT.format(agents_descriptions=prompts)

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]

        return self.agent.invoke({"messages": messages})
