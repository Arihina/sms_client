import base64

from models.user import User


class BasicAuth:
    """
    A class for generating a Basic Authentication string.
    """

    @staticmethod
    def get_encode(user: User) -> str:
        """
        Generates the Basic Authentication string.

        :param user: User object.
        :return: Basic Authentication str.
        """

        return "Basic " + base64.b64encode(f"{user.name}:{user.password}".encode()).decode()
