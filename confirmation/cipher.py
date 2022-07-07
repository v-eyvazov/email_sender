from cryptography.fernet import Fernet
from confirmation.utils import open_relative


def encrypt(email):
    fkey = open_relative("../secret_key/symmetric_key.txt", "rb")
    key = fkey.read()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(email.encode())
    return encrypted.decode()


def decrypt(email):
    fkey = open_relative("../secret_key/symmetric_key.txt", "rb")
    key = fkey.read()
    cipher = Fernet(key)
    decrypted_email = cipher.decrypt(email.encode())
    return decrypted_email.decode()
