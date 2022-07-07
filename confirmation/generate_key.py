from cryptography.fernet import Fernet

if __name__ == '__main__':
    key = Fernet.generate_key()
    fkey = open("../secret_key/symmetric_key.txt", "wb")
    fkey.write(key)
