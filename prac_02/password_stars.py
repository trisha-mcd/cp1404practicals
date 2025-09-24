"""
Practical 2 - Password Program
"""

MINIMUM_PASSWORD_LENGTH = 5 # set variable

user_password = input("Password: ")
while len(user_password) < MINIMUM_PASSWORD_LENGTH:
    print("Invalid")
    user_password = input("Password: ")
print("*" * len(user_password))
