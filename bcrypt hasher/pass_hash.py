import bcrypt

#stored password
password = "password123"

#convert password
password_bytes = password.encode("utf-8")

#generate salt
salt = bcrypt.gensalt()

#hash the password
password_hash = bcrypt.hashpw(password_bytes, salt)

print(password_hash)

#entered password
entered_password = "password000"

#convert entered password
entered_bytes = entered_password.encode("utf-8")

#hash the password
entered_hash = bcrypt.hashpw(entered_bytes, salt)

#compare the passwords