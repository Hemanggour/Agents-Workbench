from abc import abstractmethod
from typing import Any, List

from langchain.chat_models import init_chat_model
from langchain_core.tools import BaseTool

from workbench.utils.config.settings import settings

from .tool_manager import BaseToolManager


class BaseAgent:
    def __init__(self, model: str = None, model_provider: str = None) -> None:

        self.model = model if model else settings.MODEL
        self.model_provider = (
            model_provider if model_provider else settings.MODEL_PROVIDER
        )
        self.llm = init_chat_model(model=self.model, model_provider=self.model_provider)
        self.tools: List[BaseTool] = []
        self.description = ""
        self.agent = None

    @abstractmethod
    def run(self, tool_manager: BaseToolManager) -> Any:
        pass
