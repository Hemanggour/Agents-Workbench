import os
from typing import Any, Dict, List

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configuration settings for the application"""

    # Language Model Configuration
    MODEL = os.getenv("MODEL", "gemini-2.0-flash")
    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "google_genai")
    MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", "0.7"))

    DEFAULT_MODEL_CONFIG = {
        "model": MODEL,
        "provider": MODEL_PROVIDER,
        "temperature": MODEL_TEMPERATURE,
    }

    # Memory Configuration
    MEMORY_WINDOW_SIZE = int(os.getenv("MEMORY_WINDOW_SIZE", "20"))

    # Email Configuration
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
    EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "False").lower() == "true"
    EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", "30"))
    EMAIL_DEFAULT_SENDER = os.getenv("EMAIL_DEFAULT_SENDER", "")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

    # Web Scraper Configuration
    WEB_USER_AGENT = os.getenv(
        "WEB_USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  # noqa
    )
    WEB_CONTENT_LIMIT = int(os.getenv("WEB_CONTENT_LIMIT", "5000"))
    WEB_LINKS_LIMIT = int(os.getenv("WEB_LINKS_LIMIT", "20"))
    WEB_REQUEST_TIMEOUT = int(os.getenv("WEB_REQUEST_TIMEOUT", "10"))
    WEB_SEARCH_MAX_RESULTS = os.getenv("WEB_SEARCH_MAX_RESULTS", 5)
    WEB_SEARCH_TYPE = os.getenv(
        "WEB_SEARCH_TYPE", "text"
    )  # text, images, videos, news. This is only default value and can be overridden per search by LLM. # noqa

    # System Command Configuration
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "30"))
    DANGEROUS_COMMANDS: List[str] = [
        "rm -rf /",
        "del /f /s /q",
        "format",
        "mkfs",
        "dd if=",
        "shutdown",
        "reboot",
        "halt",
        "sudo rm",
        "rm -rf *",
    ]

    # Network Configuration
    PING_COUNT = int(os.getenv("PING_COUNT", "4"))
    DOWNLOAD_CHUNK_SIZE = int(os.getenv("DOWNLOAD_CHUNK_SIZE", "8192"))
    DOWNLOAD_TIMEOUT = int(os.getenv("DOWNLOAD_TIMEOUT", "30"))

    # Agent Configuration
    AGENT_NAME = os.getenv("AGENT_NAME", "ThinkPad")
    VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"
    AGENT_MAX_ITERATIONS = int(os.getenv("AGENT_MAX_ITERATIONS", "15"))
    AGENT_MAX_EXECUTION_TIME = int(os.getenv("AGENT_MAX_EXECUTION_TIME", "60"))

    # HASHING Configuration
    HASHING_ALGORITHM = os.getenv("HASHING_ALGORITHM", "sha256")

    # Default directories and files to ignore
    DISABLE_SMART_IGNORE = False
    DEFAULT_IGNORE_DIRS = {
        # Virtual environments
        "venv",
        "env",
        ".venv",
        ".env",
        "virtualenv",
        "ENV",
        "env.bak",
        "venv.bak",
        # Package managers and dependencies
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        "pip-wheel-metadata",
        "site-packages",
        "dist",
        "build",
        "egg-info",
        ".eggs",
        "wheels",
        # Version control
        ".git",
        ".hg",
        ".svn",
        ".bzr",
        "_darcs",
        # IDEs and editors
        ".vscode",
        ".idea",
        ".vs",
        ".atom",
        ".sublime-project",
        ".sublime-workspace",
        # OS specific
        ".DS_Store",
        "Thumbs.db",
        "__MACOSX",
        # Logs and temporary files
        "logs",
        "log",
        "tmp",
        "temp",
        ".tmp",
        ".temp",
        # Documentation builds
        "_build",
        "docs/_build",
        "site",
        ".docusaurus",
        # Other common ignore patterns
        ".mypy_cache",
        ".tox",
        ".nox",
        ".coverage",
        "htmlcov",
        ".nyc_output",
        "coverage",
        ".sass-cache",
        ".parcel-cache",
        ".next",
        ".nuxt",
    }

    DEFAULT_IGNORE_FILES = {
        # Compiled files
        "*.pyc",
        "*.pyo",
        "*.pyd",
        "*.class",
        "*.dll",
        "*.exe",
        "*.o",
        "*.a",
        "*.lib",
        "*.so",
        # Archives
        "*.zip",
        "*.tar",
        "*.tar.gz",
        "*.rar",
        "*.7z",
        # Images (usually not searched)
        "*.jpg",
        "*.jpeg",
        "*.png",
        "*.gif",
        "*.bmp",
        "*.ico",
        "*.svg",
        "*.webp",
        # Videos and audio
        "*.mp4",
        "*.avi",
        "*.mov",
        "*.mp3",
        "*.wav",
        "*.flac",
        # Documents (can be large)
        "*.pdf",
        "*.doc",
        "*.docx",
        "*.xls",
        "*.xlsx",
        "*.ppt",
        "*.pptx",
        # Database files
        "*.db",
        "*.sqlite",
        "*.sqlite3",
        # Lock files
        "package-lock.json",
        "yarn.lock",
        "Pipfile.lock",
        "poetry.lock",
        # Other
        "*.min.js",
        "*.min.css",
        ".gitignore",
        ".gitkeep",
    }

    def get_all_config(self) -> Dict[str, Any]:
        """Return all configuration as a dictionary"""
        return {
            "model_config": self.DEFAULT_MODEL_CONFIG,
            "memory": {
                "window_size": self.MEMORY_WINDOW_SIZE,
            },
            "email": {
                "smtp_server": self.SMTP_SERVER,
                "smtp_port": self.SMTP_PORT,
                "use_tls": self.EMAIL_USE_TLS,
                "use_ssl": self.EMAIL_USE_SSL,
                "timeout": self.EMAIL_TIMEOUT,
                "default_sender": self.EMAIL_DEFAULT_SENDER,
                "password": self.EMAIL_PASSWORD,
            },
            "web": {
                "user_agent": self.WEB_USER_AGENT,
                "content_limit": self.WEB_CONTENT_LIMIT,
                "links_limit": self.WEB_LINKS_LIMIT,
                "timeout": self.WEB_REQUEST_TIMEOUT,
            },
            "system": {
                "command_timeout": self.COMMAND_TIMEOUT,
                "dangerous_commands": self.DANGEROUS_COMMANDS,
            },
            "network": {
                "ping_count": self.PING_COUNT,
                "download_chunk_size": self.DOWNLOAD_CHUNK_SIZE,
                "download_timeout": self.DOWNLOAD_TIMEOUT,
            },
            "file": {
                "disable_smart_ignore": self.DISABLE_SMART_IGNORE,
                "ignore_dirs": self.DEFAULT_IGNORE_DIRS,
                "ignore_files": self.DEFAULT_IGNORE_FILES,
            },
            "agent": {
                "name": self.AGENT_NAME,
                "verbose": self.VERBOSE,
                "max_iterations": self.AGENT_MAX_ITERATIONS,
                "max_execution_time": self.AGENT_MAX_EXECUTION_TIME,
            },
            "hashing": {
                "hashing_algorithm": self.HASHING_ALGORITHM,
            },
        }


settings = Settings()
