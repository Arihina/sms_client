import json

from models.http.base import BaseHttp


class HttpResponse(BaseHttp):
    def __init__(self, version: str, date: str,
                 content_type: str, content_length: int,
                 status_code: str, body: dict[str, str]):
        """
        Initializes a HttpResponse object representing the HTTP response.

        :param version: The HTTP version.
        :param date: The date the message was created.
        :param status_code: The HTTP response status code.
        :param content_type: The Content-Type header.
        :param content_length: The Content-Length header.
        :param body: A dictionary representing the body of the HTTP.
        """

        super().__init__(version, body, content_type, content_length)
        self.__status_code: str = status_code
        self.__date: str = date

    @property
    def status_code(self) -> str:
        return self.__status_code

    @property
    def date(self) -> str:
        return self.__date

    @classmethod
    def from_bytes(cls, binary_data: bytes):
        """
        Serializes the HttpResponse object from a bytes.

        :param binary_data: The byte string.
        :return: HttpResponse object.
        """

        headers_bytes, body_bytes = binary_data.split(b'\r\n\r\n', 1)

        body = json.loads(body_bytes.decode())
        body_dict = {k: str(v) for k, v in body.items()}

        headers = headers_bytes.decode().replace('www-authenticate: Basic\r\n', '').split('\r\n')
        version, status_code = headers[0].split(' ', 1)
        date = headers[1][6::]
        content_length = int(headers[3][16::])
        content_type = headers[4][14::]

        return cls(
            version=version,
            status_code=status_code,
            date=date,
            content_length=content_length,
            content_type=content_type,
            body=body_dict
        )

    def __repr__(self):
        return (f"headers: {{\n"
                f"\t version: {self.version}\n"
                f"\t status_code: {self.status_code}\n"
                f"\t date: {self.date}\n"
                f"\t content-length: {self.content_length}\n"
                f"\t content-type: {self.content_type}\n"
                f"}}\n"
                f"body:\n"
                f"\t{self.body}")

    def __str__(self):
        return (f"Status code {self.status_code}\n"
                f"Body\n"
                f"\t{self.body}")
