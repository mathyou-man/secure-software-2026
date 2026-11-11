#create a restricted environment with limited built-in functions (a whitelist)
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

restricted_env = {'__builtins__': {'print':print, 'open':open}} 

#safe code
safe_code = 'print("That is safe code")'

#dangerous code
dangerous_code = 'open("credentials.txt", "r")'

clear_screen()

#execute the safe code
try:
    exec(dangerous_code, restricted_env)
except NameError as e:
    print(f"Error: {e}")

input()