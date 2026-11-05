from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('file.key', 'wb') as filekey:
    filekey.write(key)