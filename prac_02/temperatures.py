"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """This is the main function for the temperature conversion program"""
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            fahrenheit = calculate_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif user_choice == "F":
            celsius = calculate_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        user_choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius():
    """Calculate Celsius degrees"""
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit():
    """Calculate Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
