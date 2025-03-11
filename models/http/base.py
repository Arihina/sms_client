class BaseHttp:
    def __init__(self, version: str, content_type: str = None,
                 content_length: int = None, body: dict[str, str] = None):
        """
        Initializes a BaseHttp object representing a basic HTTP.

        :param version: The HTTP version.
        :param content_type: The Content-Type header.
        :param content_length: The Content-Length header.
        :param body: A dictionary representing the body of the HTTP.
        """

        self.__version: str = version
        self.__content_type: str | None = content_type
        self.__content_length: int | None = content_length
        self.__body: dict[str, str] | None = body

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

    @version.setter
    def version(self, version: str) -> None:
        self.__version = version

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        self.__content_type = content_type

    @content_length.setter
    def content_length(self, content_length: int) -> None:
        self.__content_length = content_length

    @body.setter
    def body(self, body: dict[str, str]) -> None:
        self.__body = body
