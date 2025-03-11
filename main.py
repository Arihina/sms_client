import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    client.connect(('localhost', 4010))
    request = b"GET /send_sms HTTP/1.1\r\nHost: localhost:4010\r\n\r\n"
    client.sendall(request)

    response = b""
    while True:
        chunk = client.recv(4096)

        if len(chunk) == 0:
            break

        response = response + chunk

    print(f"Received:\n{response.decode()}")

    client.close()
