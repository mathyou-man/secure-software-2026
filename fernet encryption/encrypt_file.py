from cryptography.fernet import Fernet

#gets the key from the key file
with open('file.key', 'rb') as filekey:
    key = filekey.read()

#injects key to help fernet use it
fernet = Fernet(key)

#opens file to encrypt
with open('encrypt_me.docx', 'rb') as file:
    original = file.read()

#writes encrypted data
encrypted = fernet.encrypt(original)

with open('encrypt_me.docx', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

    