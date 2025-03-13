class User:
    def __init__(self, name: str, password: str):
        """
        Initializes a User object.

        :param name: The user's name.
        :param password: The user's password.
        """
        self.__name = name
        self.__password = password

    @property
    def name(self) -> str:
        return self.__name

    @property
    def password(self) -> str:
        return self.__password

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @password.setter
    def password(self, password: str) -> None:
        self.__password = password

    def __repr__(self):
        return (f"User\n"
                f"\tname: {self.__name}\n"
                f"\tpassword: {self.__password}")
