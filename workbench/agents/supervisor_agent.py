from typing import Any

from langgraph_supervisor import create_supervisor

from workbench.agents.research_agent import ResearchAgent
from workbench.agents.system_agent import SystemAgent
from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.prompts import SUPERVISOR_AGENT_PROMPT


class SupervisorAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        research_agent = ResearchAgent()
        system_agent = SystemAgent()

        agents_list = [
            research_agent,
            system_agent,
        ]

        self.agent = create_supervisor(
            name="supervisor",
            model=self.llm,
            agents=[agent.agent for agent in agents_list],
            prompt=self.__prompt_builder(agents_list),
        ).compile()

    def __prompt_builder(self, agents: list[BaseAgent]) -> str:
        prompts = "\n".join(
            [f"{agent.agent.name}: {agent.description}\n" for agent in agents]
        )

        return SUPERVISOR_AGENT_PROMPT.format(agents_descriptions=prompts)

    def run(self, query: str) -> Any:
        messages = [{"role": "user", "content": query}]

        return self.agent.invoke({"messages": messages})
