from dataclasses import dataclass


@dataclass(frozen=True)
class URL:
    """
    Initializes a URL object.

    :param host: The hostname of the server.
    :param port: The port number to connect to.
    :param uri: The URI or route on the server.
    """
    host: str
    port: int
    uri: str

    def __repr__(self):
        return (f"URL:\n"
                f"\thost: {self.host}\n"
                f"\tport: {self.port}\n"
                f"\turi: {self.uri}")
