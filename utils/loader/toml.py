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
        try:
            with open(path, "rb") as f:
                data = tomllib.load(f)

            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {path}")
        except tomllib.TOMLDecodeError as e:
            raise tomllib.TOMLDecodeError(f"Error decoding TOML file: {e}")
        except ValueError as e:
            raise ValueError(f"Value error in TOML file: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error occurred: {e}")
