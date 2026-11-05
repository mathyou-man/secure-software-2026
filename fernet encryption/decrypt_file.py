from cryptography.fernet import Fernet

#gets the key from the key file
with open('file.key', 'rb') as filekey:
    key = filekey.read()

#injects key to help fernet use it
fernet = Fernet(key)

with open('encrypt_me.docx', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('encrypt_me.docx', 'wb') as dec_file:
    dec_file.write(decrypted)