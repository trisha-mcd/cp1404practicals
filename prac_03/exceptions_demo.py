"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When the input isn't an integer, such as a string, empty string or float number
2. When will a ZeroDivisionError occur?
- When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- By adding an if else statement
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
