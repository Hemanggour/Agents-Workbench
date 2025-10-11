from workbench.agents.supervisor_agent import SupervisorAgent

if __name__ == "__main__":
    agent = SupervisorAgent()

    query = input("Me: ")

    while query not in ["exit", "quit"]:
        result = agent.run(query)
        response = result["messages"][-1].content
        print(f"AI: {response}")

        query = input("Me: ")
