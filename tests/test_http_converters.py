import base64
import json

import pytest

from models.http.request import HttpRequest
from models.http.response import HttpResponse


def test_to_binary():
    username = "user"
    password = "12345"

    auth = f"{username}:{password}".encode('utf-8')

    data = {
        "sender": "88005553535",
        "recipient": "88005553536",
        "message": "test"
    }

    body = json.dumps(data).encode('utf-8')

    request = HttpRequest(
        "POST", "/send_sms", "HTTP/1.1",
        "localhost:4010", "Basic " + base64.b64encode(auth).decode(), "application/json",
        len(body), data).to_bytes()

    request_binary = (b'POST /send_sms HTTP/1.1\r\n'
                      b'Host: localhost:4010\r\n'
                      b'Authorization:Basic dXNlcjoxMjM0NQ==Content-Type: application/json\r\n'
                      b'Content-Length: 72\r\n'
                      b'\r\n{"sender": "88005553535", "recipient": "88005553536", "message": "test"}')

    assert request == request_binary


def test_from_binary():
    request1 = HttpResponse.from_bytes(
        b'HTTP/1.1 200 OK\r\n'
        b'date: Tue, 11 Mar 2025 14:16:15 GMT\r\n'
        b'server: uvicorn\r\n'
        b'content-length: 42\r\n'
        b'content-type: application/json\r\n\r\n{"status":"success","message_id":"123456"}'
    )
    request2 = HttpResponse("HTTP/1.1", "Tue, 11 Mar 2025 14:16:15 GMT",
                            "application/json", 42, "200 OK",
                            {"status": "success", "message_id": "123456"})

    assert request1.__repr__() == request2.__repr__()


if __name__ == '__main__':
    pytest.main()
