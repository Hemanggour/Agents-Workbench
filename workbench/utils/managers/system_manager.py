from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.system_tools import SystemTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class SystemManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = SystemTools()

        return [
            tools.execute_command_tool,
            tools.get_system_info_tool,
            tools.get_running_processes_tool,
            tools.get_disk_usage_tool,
            tools.get_memory_usage_tool,
            tools.get_network_info_tool,
        ]
