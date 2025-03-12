import socket

from utils.loader.toml import TomlLoader
from utils.parser.url import UrlParser

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    loader = TomlLoader()
    config = loader.load_file('config.toml')

    username = config['user']['name']
    password = config['user']['password']
    server_url = config['servers']['sms']['url']

    host, port, uri = UrlParser.parse(server_url)

    client.connect((host, port))

    request = (b'POST /send_sms HTTP/1.1\r\n'
               b'Host: localhost:4010\r\n'
               b'Authorization:Basic dXNlcjoxMjM0NQ==Content-Type: application/json\r\n'
               b'Content-Length: 72\r\n'
               b'\r\n{"sender": "88005553535", "recipient": "88005553536", "message": "test"}')

    client.sendall(request)

    response = b""
    while True:
        chunk = client.recv(4096)

        if len(chunk) == 0:
            break

        response = response + chunk

    print(response)

    client.close()
