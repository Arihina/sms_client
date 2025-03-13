from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """
    Initializes a User object.

    :param name: The user's name.
    :param password: The user's password.
    """
    name: str
    password: str

    def __repr__(self):
        return (f"User\n"
                f"\tname: {self.__name}\n"
                f"\tpassword: {self.__password}")
