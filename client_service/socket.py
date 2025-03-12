import socket


class SocketClient:
    """
    Client implementation using socket.
    """

    def __init__(self):
        """
        Initializes a new SocketClient object.
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open_connection(self, host: str, port: int) -> None:
        """
        Opens a connection to the specified host and port.

        :param host: The hostname of the server.
        :param port: The port number to connect to.
        :return: None
        """
        try:
            self.client.connect((host, port))
        except socket.error as e:
            raise socket.error(e)

    def close_connection(self) -> None:
        """
        Closes the connection to the server.

        :return: None
        """
        try:
            self.client.close()
        except socket.error as e:
            raise socket.error(e)

    def send_data(self, request: bytes) -> None:
        """
        Sends data to the connected server.

        :param request: The data to be sent.
        :return: None
        """
        try:
            self.client.sendall(request)
        except socket.error as e:
            raise socket.error(e)

    def receive_date(self) -> bytes:
        """
        Receives data from the connected server.

        :return: The received data.
        """
        try:
            response = b""

            while True:
                chunk = self.client.recv(4096)

                if len(chunk) == 0:
                    break

                response = response + chunk

            return response
        except socket.error as e:
            raise socket.error(e)
