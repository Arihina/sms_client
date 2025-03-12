from unittest.mock import MagicMock

import pytest

from client_service.socket import SocketClient


@pytest.fixture
def get_mock_client():
    client = SocketClient()
    client.client = MagicMock()

    return client


def test_open_connection(get_mock_client):
    client = get_mock_client

    client.open_connection("localhost", 4010)
    client.client.connect.assert_called_with(("localhost", 4010))


def test_close_connection(get_mock_client):
    client = get_mock_client

    client.close_connection()
    client.client.close.assert_called_once()


def test_send_data(get_mock_client):
    client = get_mock_client

    data = b"Some test data"
    client.send_data(data)
    client.client.sendall.assert_called_once_with(data)


def test_receive_data(get_mock_client):
    client = get_mock_client

    client.client.recv.side_effect = [b"Test chunk 1 ", b"Test chunk 2", b""]
    received_data = client.receive_date()
    assert received_data == b"Test chunk 1 Test chunk 2"
    client.client.recv.assert_called()


if __name__ == '__main__':
    pytest.main()
