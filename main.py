import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    client.connect(('localhost', 4010))

    request = b""

    client.sendall(request)

    response = b""
    while True:
        chunk = client.recv(4096)

        if len(chunk) == 0:
            break

        response = response + chunk

    print(response)

    client.close()
