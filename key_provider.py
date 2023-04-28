from base64 import b64encode
from getpass import getpass


def get_protection_key():
    protection_user_key = get_user_key()

    while not is_valid_protection_key_input(protection_user_key):
        print("Key should have length 4 or more symbols")
        protection_user_key = get_user_key()

    key = convert_protection_key_to_base64_format(protection_user_key)

    return key


def convert_protection_key_to_32_length(key):
    return (key * 32)[:32]


def convert_protection_key_to_base64_format(key):
    key_32_length = convert_protection_key_to_32_length(key)
    key_bytes = key_32_length.encode("ascii")
    key_base64 = b64encode(key_bytes)

    return key_base64


def is_valid_protection_key_input(key):
    if key is None or len(key) < 4:
        return False

    return True


def get_user_key():
    return getpass("Please enter a protection key:\n")