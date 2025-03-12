from abc import ABCMeta, abstractmethod
from typing import Any


class BaseLoader(metaclass=ABCMeta):
    """
    Base class for implement config file loader
    """

    @abstractmethod
    def load_file(self, path: str) -> dict[str, Any]:
        """
        Loads a configuration file.
        This method must be implemented by subclasses to load a configuration
        file. The specific file format and loading
        mechanism are determined by the subclass.

        :param path: The path to the configuration file to load.
        :return: A dictionary with configuration data. Keys are strings, and values can be any.
        """
        pass
