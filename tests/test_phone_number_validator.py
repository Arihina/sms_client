import os
import sys

import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from utils.validator.phone_number import PhoneNumberValidator


def test_validate_valid():
    assert PhoneNumberValidator.validate('88005553535') is True
    assert PhoneNumberValidator.validate('89111111111') is True


def test_validate_invalid():
    assert PhoneNumberValidator.validate('880055535') is False
    assert PhoneNumberValidator.validate('+78005553535') is False
    assert PhoneNumberValidator.validate('880055535355') is False
    assert PhoneNumberValidator.validate('8800abc35355') is False
    assert PhoneNumberValidator.validate('') is False


def test_validate_e164_valid():
    assert PhoneNumberValidator.validate_e164('+79005553535') is True
    assert PhoneNumberValidator.validate_e164('+15151515151515') is True


def test_validate_e164_invalid():
    assert PhoneNumberValidator.validate_e164('') is False
    assert PhoneNumberValidator.validate_e164('++5151515151515') is False
    assert PhoneNumberValidator.validate_e164("+151515151515151515151515") is False
    assert PhoneNumberValidator.validate_e164("151515151515151") is False


if __name__ == '__main__':
    pytest.main()
