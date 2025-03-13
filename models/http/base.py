class BaseHttp:
    def __init__(self, version: str, body: dict[str, str],
                 content_type: str = "",
                 content_length: int = 0):
        """
        Initializes a BaseHttp object representing a basic HTTP.

        :param version: The HTTP version.
        :param content_type: The Content-Type header.
        :param content_length: The Content-Length header.
        :param body: A dictionary representing the body of the HTTP.
        """

        self.__version: str = version
        self.__content_type: str = content_type
        self.__content_length: int = content_length
        self.__body: dict[str, str] = body

    @property
    def version(self) -> str:
        return self.__version

    @property
    def content_type(self) -> str:
        return self.__content_type

    @property
    def content_length(self) -> int:
        return self.__content_length

    @property
    def body(self) -> dict[str, str]:
        return self.__body
