from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.security_tools import SecurityTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class SecurityManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = SecurityTools()

        return [
            tools.hash_file_tool,
        ]
