import tomllib
from typing import Any

from utils.loader.base import BaseLoader


class TomlLoader(BaseLoader):
    """
    Class implement loader for .toml config file
    """

    def load_file(self, path: str) -> dict[str, Any]:
        """
        Loads a TOML configuration file from the path.

        :param path: The path to the configuration file to load.
        :return: A dictionary with configuration data. Keys are strings, and values can be any.
        """

        with open(path, "rb") as f:
            data = tomllib.load(f)

        return data
