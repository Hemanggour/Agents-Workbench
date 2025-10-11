from typing import Any, Dict, List

from langchain.memory import ConversationBufferMemory
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.prebuilt import create_react_agent

from workbench.utils.core.base.agent import BaseAgent
from workbench.utils.managers.web_manager import WebManager
from workbench.utils.prompts import RESEARCH_PROMPT


class ResearchAgent(BaseAgent):
    def __init__(self, model: str = None, model_provider: str = None) -> None:
        super().__init__(model, model_provider)

        self.tools = WebManager.get_tools()

        # Initialize conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True, output_key="output"
        )

        # Create agent without memory parameter
        self.agent = create_react_agent(
            name="research_agent",
            model=self.llm,
            tools=self.tools,
            prompt=RESEARCH_PROMPT,
        )

        self.description = f"""# Research Agent: This agent is used to get the results from web.
        ## Abilities:
        {"\n- ".join([tool.name for tool in self.tools])}
        """

    def _format_chat_history(self, history: List[Dict]) -> List[Dict]:
        """Convert the chat history into the format expected by the agent."""
        formatted_history = []
        for message in history:
            if isinstance(message, dict):
                formatted_history.append(message)
            elif isinstance(message, (HumanMessage, AIMessage)):
                formatted_history.append(
                    {
                        "role": (
                            "user" if isinstance(message, HumanMessage) else "assistant"
                        ),
                        "content": message.content,
                    }
                )
        return formatted_history

    def run(self, query: str) -> Any:
        # Get chat history from memory
        chat_history = self.memory.load_memory_variables({})

        # Prepare messages with chat history
        messages = []

        # Add chat history if it exists
        if chat_history.get("chat_history"):
            for msg in chat_history["chat_history"]:
                if isinstance(msg, (HumanMessage, AIMessage)):
                    messages.append(
                        {
                            "role": (
                                "user" if isinstance(msg, HumanMessage) else "assistant"
                            ),
                            "content": msg.content,
                        }
                    )

        # Add the new query
        messages.append({"role": "user", "content": query})

        # Run the agent
        response = self.agent.invoke({"messages": messages})

        # Save the interaction to memory
        self.memory.save_context(
            {"input": query},
            {
                "output": (
                    response.get("messages", [])[-1].content
                    if isinstance(response, dict) and response.get("messages")
                    else "No response"
                )
            },
        )

        return response
