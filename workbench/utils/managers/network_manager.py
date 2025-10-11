from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.network_tools import NetworkTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class NetworkManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = NetworkTools()

        return [
            tools.ping_host_tool,
            tools.download_file_tool,
        ]
