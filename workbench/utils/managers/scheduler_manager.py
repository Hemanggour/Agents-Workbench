from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.scheduler_tools import SchedulerTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class SchedulerManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = SchedulerTools()

        return [
            tools.schedule_task_tool,
            tools.list_scheduled_tasks_tool,
            tools.remove_scheduled_task_tool,
        ]
