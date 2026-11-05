import hashlib
import os

def clear_screen():
    '''Clears the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def sign_up():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password == confirm_password:
        enc = password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        print("Register successful.")
    else:
        print("Passwords do not match.")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    enc = password.encode()
    hash2 = hashlib.md5(enc).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    if stored_email == email and stored_pwd == hash2:
        print("Logged in successfully.")
    else:
        print("Login failed.")

exit_flag = False
while exit_flag == False:
    clear_screen()
    print("Matt Corp Interface\n")
    print(" (1)Log In")
    print(" (2)Sign Up")
    print(" (3)Exit")
    decision = input("\n > ")

    if decision == "1":
        login()
    elif decision == "2":
        sign_up()
    elif decision == "3":
        exit_flag = True
    else:
        print("Invalid input.")

    input()