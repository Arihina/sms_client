import json

from models.http.base import BaseHttp


class HttpRequest(BaseHttp):
    def __init__(self, method: str, uri: str, version: str, host: str, auth: str,
                 content_type: str = None, content_length: int = None,
                 body: dict[str, str] = None):
        """
        Initializes a HttpRequest object representing the HTTP request.

        :param method: The HTTP method.
        :param uri: The URI (Uniform Resource Identifier).
        :param version: The HTTP version.
        :param host: The host header.
        :param auth: The Authorization header.
        :param content_type: The Content-Type header.
        :param content_length: The Content-Length header.
        :param body: A dictionary representing the body of the HTTP.
        """

        super().__init__(version, content_type, content_length, body)
        self.__method: str = method
        self.__uri: str = uri
        self.__host: str = host
        self.__auth: str = auth

    @property
    def method(self) -> str:
        return self.__method

    @property
    def uri(self) -> str:
        return self.__uri

    @property
    def host(self) -> str:
        return self.__host

    @property
    def auth(self) -> str:
        return self.__auth

    @method.setter
    def method(self, method: str) -> None:
        self.__method = method

    @uri.setter
    def uri(self, uri: str) -> None:
        self.__uri = uri

    @host.setter
    def host(self, host: str) -> None:
        self.__host = host

    @auth.setter
    def auth(self, auth: str) -> None:
        self.__auth = auth

    def to_bytes(self) -> bytes:
        """
        Serializes the HttpRequest object to a bytes.

        :return: The bytes representing the HTTP request.
        """

        request = f"{self.method} {self.uri} {self.version}\r\n".encode()

        headers = f"Host: {self.host}\r\n"
        headers += f"Authorization:{self.auth}"
        headers += f"Content-Type: {self.content_type}\r\n" if self.content_type else ""
        headers += f"Content-Length: {self.content_length}\r\n\r\n" if self.content_length else "\r\n"
        headers = headers.encode()

        body = json.dumps(self.body).encode()

        return request + headers + body

    def __repr__(self):
        return (f"method {self.method}\n"
                f"uri {self.uri}\n"
                f"headers: {{\n"
                f"\t version: {self.version}\n"
                f"\t content-length: {self.content_length}\n"
                f"\t content-type: {self.content_type}\n"
                f"}}\n"
                f"body:\n"
                f"\t{self.body}")
