from workbench.agents.network_agent import NetworkAgent
from workbench.agents.research_agent import ResearchAgent
from workbench.agents.supervisor_agent import SupervisorAgent
from workbench.agents.system_agent import SystemAgent


def main():
    research_agent = ResearchAgent()
    system_agent = SystemAgent()
    network_agent = NetworkAgent()

    agent = SupervisorAgent(
        sub_agents_list=[
            research_agent,
            system_agent,
            network_agent,
        ]
    )

    try:
        query = input("Me: ")

        while query not in ["exit", "quit"]:

            result = agent.run(query)
            response = result["messages"][-1].content
            print(f"AI: {response}")

            query = input("Me: ")

    except KeyboardInterrupt:
        print("\nGoodbye!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
