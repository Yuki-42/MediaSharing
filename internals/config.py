"""
Contains the Config class for the project.
"""

# Standard Imports
from os import environ

# Package Relative Imports
from .logging_ import createLogger, SuppressedLoggerAdapter


class Config:
    """
    The config class for the application. Used to allow easier access to the config values in .env
    """
    # Type Hints
    logger: SuppressedLoggerAdapter

    def __init__(self) -> None:
        """
        Initializes the Config class.
        """
        self.logger = createLogger("Config")

    @property
    def debug(self) -> bool:
        """
        Gets the debug value from the environment variables.

        Returns:
            bool: The debug value.
        """
        return environ.get("DEBUG") == "True"

    @property
    def loggingLevel(self) -> str:
        """
        Gets the logging level from the environment variables.

        Returns:
            str: The logging level.
        """
        return environ.get("LOGGING_LEVEL").upper()

    @property
    def ip(self) -> str:
        """
        Gets the ip from the environment variables.

        Returns:
            str: The ip.
        """
        return environ.get("IP")

    @property
    def port(self) -> int:
        """
        Gets the port from the environment variables.

        Returns:
            int: The port.
        """
        return int(environ.get("PORT"))

