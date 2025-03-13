class BaseHttp:
    def __init__(self, version: str, body: dict[str, str]):
        """
        Initializes a BaseHttp object representing a basic HTTP.

        :param version: The HTTP version.
        :param body: A dictionary representing the body of the HTTP.
        """

        self.__version: str = version
        self.__body: dict[str, str] = body

    @property
    def version(self) -> str:
        return self.__version

    @property
    def body(self) -> dict[str, str]:
        return self.__body
