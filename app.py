import json
import socket
import tomllib
from typing import Any

from client_service.socket import SocketClient
from models.http.request import HttpRequest
from models.http.response import HttpResponse
from models.url import URL
from models.user import User
from utils.auth.basic import BasicAuth
from utils.loader.toml import TomlLoader
from utils.parser.url import UrlParser
from utils.validator.phone_number import PhoneNumberValidator


class App:
    """
    Class for launching an application in the CLI.
    """

    @staticmethod
    def load_config() -> dict[str, Any]:
        """
        Loads a TOML configuration file.

        :return: A dictionary with configuration data.
        """
        try:
            loader = TomlLoader()
            return loader.load_file('config.toml')
        except FileNotFoundError as e:
            print("Error: config.toml file not found.")
            exit(1)
        except tomllib.TOMLDecodeError as e:
            print(f"Error: TOML syntax error in config.toml: {e}")
            exit(1)
        except ValueError as e:
            print(f"Error: Invalid value in the configuration file: {e}")
            exit(1)
        except Exception as e:
            print(f"Unknown error loading configuration: {e}")
            exit(1)

    @staticmethod
    def get_input_date() -> tuple[str, str, str] | None:
        """
        Receives data input and verifies its validity

        :return: A tuple containing the sender's number, recipient's number and message text if both numbers are valid.
                 Returns None if either number is invalid.
        """
        sender_number = input("Enter the sender's number -> ")
        if not PhoneNumberValidator().validate(sender_number):
            if not PhoneNumberValidator().validate_e164(sender_number):
                print("Incorrect sender's number")
                return None

        recipient_number = input("Enter the recipient's number -> ")
        if not PhoneNumberValidator().validate(sender_number):
            if not PhoneNumberValidator().validate_e164(recipient_number):
                print("Incorrect recipient's number")
                return None

        message = input("Enter the text of the message -> ")

        return sender_number, recipient_number, message

    @staticmethod
    def run() -> None:
        """
        Runs the app.

        :return: None
        """
        config = App.load_config()

        user = User(config['user']['name'], config['user']['password'])
        url = URL(*UrlParser.parse(config['servers']['sms']['url']))

        client = SocketClient()

        try:
            client.open_connection(url.host, url.port)
        except socket.error as e:
            print("Error connecting to the server")
            exit(1)

        while True:
            print("Menu:\n"
                  "(1) Send message\n"
                  "(0) Exit")

            choice = input("-> ")

            if choice == '1':
                try:
                    data = App.get_input_date()
                except ValueError as e:
                    print(f"Error: Invalid value in inputs data: {e}")
                    continue

                if data is None:
                    continue

                auth = BasicAuth.get_encode(user)

                body = {
                    "sender": data[0],
                    "recipient": data[1],
                    "message": data[2]
                }
                content_length = len(json.dumps(body).encode())

                request = HttpRequest("POST", url.uri, "HTTP/1.1",
                                      url.host + ':' + str(url.port), auth,
                                      "application/json", content_length, body).to_bytes()

                try:
                    client.send_data(request)
                except socket.error as e:
                    print("Error sending message to the server")
                    exit(1)

                try:
                    response = client.receive_date()
                    response = HttpResponse.from_bytes(response)

                    print(response)
                except socket.error as e:
                    print("Error receiving data from the server")
                    exit(1)

            elif choice == '0':
                print("Exit")
                try:
                    client.close_connection()
                except socket.error as e:
                    # log
                    exit(1)
                break

            else:
                print("Invalid value")
