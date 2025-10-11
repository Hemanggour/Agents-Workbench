import hashlib
import os

from langchain.tools import StructuredTool

from workbench.utils.config.settings import settings


class SecurityTools:
    """Handles security operations"""

    def __init__(self):
        self.hash_file_tool = StructuredTool.from_function(
            name="hash_file",
            func=self.hash_file,
            args_schema={
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to hash",
                },
                "algorithm": {
                    "type": "string",
                    "description": "Hashing algorithm to use",
                    "enum": ["md5", "sha1", "sha256", "sha512"],
                    "default": f"{settings.HASHING_ALGORITHM}",
                },
            },
            description="""Calculate the hash of a file using the specified algorithm.
            Example:
            {
                "file_path": "path/to/file.txt",
                "algorithm": "sha256"
            }
            Supported algorithms: md5, sha1, sha256, sha512""",
        )

    def hash_file(
        self, file_path: str, algorithm: str = settings.HASHING_ALGORITHM
    ) -> str:
        """Calculate file hash"""
        try:
            if not os.path.exists(file_path):
                return f"Error: File '{file_path}' does not exist"

            algorithm = algorithm.lower()
            if algorithm not in ["md5", "sha1", "sha256", "sha512"]:
                return "Error: Supported hash types are md5, sha1, sha256, sha512"

            hash_obj = getattr(hashlib, algorithm)()

            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)

            return f"{algorithm.upper()} hash of '{file_path}': {hash_obj.hexdigest()}"
        except Exception as e:
            return f"Error calculating hash: {str(e)}"
