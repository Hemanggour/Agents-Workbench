from abc import abstractmethod
from typing import List

from langchain_core.tools import BaseTool


class BaseToolManager:
    def __init__(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_tools() -> List[BaseTool]:
        pass
