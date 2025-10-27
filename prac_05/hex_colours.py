"""CP1404 Practical
Hex Colour program
providing colour code of colour"""

CODE_TO_COLOUR = {"absolutezero": "0048ba", "acidgreen": "b0bf1a", "aliceblue": "f0f8ff",
                  "amaranth": "e52b50", "amber": "ffbf00", "amethyst": "9966cc", "apricot": "fbceb1",
                  "aqua": "00ffff", "armygreen": "4b5320", "ashgrey": "b2beb5"}
colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in CODE_TO_COLOUR:
        print(CODE_TO_COLOUR[colour_name])
    else:
        print("That colour is not in the list")
    colour_name = input("Enter colour name: ")
