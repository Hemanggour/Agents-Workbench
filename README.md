# Agents Workbench

A modular and extensible framework for building and managing AI agents using LangChain and LangGraph. This project provides a foundation for creating sophisticated agent-based applications with support for research, supervision, and system-level operations.

## Features

- **Modular Architecture**: Easily extensible agent system with clear separation of concerns
- **Research Capabilities**: Built-in research agent for information gathering and analysis
- **Agent Supervision**: Supervisor agent for managing and coordinating multiple agents
- **Tool Integration**: Support for various tools including web search and data processing

## Prerequisites

- Python 3.11+
- pip (Python package manager)
- (Optional) Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hemanggour/Agents-Workbench.git
   cd Agents-Workbench
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On Unix or MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## Project Structure

```
Agents-Workbench/
├── workbench/               # Main package
│   ├── agents/              # Agent implementations
│   │   ├── research_agent.py
│   │   ├── supervisor_agent.py
│   │   └── system_agent.py
│   ├── tools/               # Custom tools for agents
│   ├── utils/               # Utility modules
│   │   ├── config/         # Configuration management
│   │   ├── core/           # Core functionality
│   │   ├── graphs/         # LangGraph definitions
│   │   ├── managers/       # Resource managers
│   │   ├── nodes/          # Graph nodes
│   │   ├── prompts/        # Prompt templates
│   │   ├── schemas/        # Data models
│   │   └── states/         # State management
│   └── main.py             # Entry point
├── docs/                   # Documentation
├── tests/                  # Test files
├── .env.example           # Example environment variables
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Usage

### Running the Research Agent

```bash
python -m workbench.main
```

This will start an interactive session where you can ask questions to the research agent.

### Available Agents

1. **Research Agent**: Performs research tasks and information gathering
   ```python
   from workbench.agents.research_agent import ResearchAgent
   agent = ResearchAgent()
   result = agent.run("Your research query here")
   ```

2. **Supervisor Agent**: Coordinates multiple agents
   ```python
   from workbench.agents.supervisor_agent import SupervisorAgent
   supervisor = SupervisorAgent()
   result = supervisor.run("Your task here")
   ```

## Configuration

Configuration is managed through environment variables. Copy `.env.example` to `.env` and update the values as needed.

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangChain](https://python.langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- Inspired by the latest advancements in AI agent architectures

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
