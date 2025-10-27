"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting and using exceptions
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)
for state_code in CODE_TO_NAME:
    print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")

# error checking using while loop (before)
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

# error checking using exceptions
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Input is incorrect")
    state_code = input("Enter short state: ").upper()


