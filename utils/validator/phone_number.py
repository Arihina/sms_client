import re


class PhoneNumberValidator:
    """
    A class to verify the validity of a phone number.
    """

    @staticmethod
    def validate(phone_number: str) -> bool:
        """
        Verifies that the phone number is correct.

        :param phone_number: The phone number string to validate.
        :return: True if the phone number is valid, False otherwise.
        """
        return bool(re.match(r"^8\d{10}$", phone_number))

    @staticmethod
    def validate_e164(phone_number: str) -> bool:
        """
        Verifies that the phone number is valid according to the E.164 format.

        :param phone_number: The phone number string to validate.
        :return: True if the phone number is valid, False otherwise.
        """
        return bool(re.match(r"^\+\d{1,15}$", phone_number))
