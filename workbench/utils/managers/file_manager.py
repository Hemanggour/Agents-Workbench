from typing import List

from langchain_core.tools import BaseTool

from workbench.tools.file_tools import FileTools
from workbench.utils.core.base.tool_manager import BaseToolManager


class FileManager(BaseToolManager):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_tools(cls) -> List[BaseTool]:
        tools = FileTools()

        return [
            tools.read_file_tool,
            tools.list_files_tool,
            tools.write_file_tool,
            tools.append_file_tool,
            tools.delete_file_tool,
            tools.get_file_info_tool,
            tools.find_duplicate_files_tool,
            tools.search_string_in_files_tool,
        ]
