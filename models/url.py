class URL:
    def __init__(self, host: str, port: int, uri: str):
        """
        Initializes a URL object.

        :param host: The hostname of the server.
        :param port: The port number to connect to.
        :param uri: The URI or route on the server.
        """
        self.__host = host
        self.__port = port
        self.__uri = uri

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def uri(self) -> str:
        return self.__uri

    @host.setter
    def host(self, host: str) -> None:
        self.__host = host

    @port.setter
    def port(self, port: int) -> None:
        self.__port = port

    @uri.setter
    def uri(self, uri: str) -> None:
        self.__uri = uri

    def __repr__(self):
        return (f"URL:\n"
                f"\thost: {self.__host}\n"
                f"\tport: {self.__port}\n"
                f"\turi: {self.__uri}")
