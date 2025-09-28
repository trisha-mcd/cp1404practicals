"""
CP1404/CP5632 - Practical
Program to print password as *
"""
MINIMUM_PASSWORD_LENGTH = 5  # set variable


def main():
    """This is the main function for the password program"""
    user_password = get_valid_password() # store the returned password
    display_password(user_password) # pass password into function


def get_valid_password():
    """Determine if password is considered valid"""
    user_password = input("Password: ")
    while len(user_password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid")
        user_password = input("Password: ")
    return user_password


def display_password(user_password):
    """Display the length of characters of the passwords"""
    print("*" * len(user_password))


main()
