from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.archive_tools import ArchiveTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class ResearchManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = ArchiveTools()

        return [
            tools.create_zip_archive_tool,
            tools.extract_zip_archive_tool,
        ]
