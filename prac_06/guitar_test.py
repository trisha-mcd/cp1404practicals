"""CP1404 - Practical
Creating a class for guitars
Started - Finished: 2:27pm
Estimated time: 40mins
Actual time:
 """
from prac_06.guitar import Guitar


def main():
    """Use a list to store all user's guitars. Keep inputting until blank name then print all details"""

    # testing
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

    guitars = []
    print("My guitars!")
    is_valid_input = False
    while not is_valid_input:
        try:
            name = input("Name: ").strip()
            if name == "":
                is_valid_input = True  # stop loop
                continue
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost} added.\n")
        except ValueError:
            print("Invalid")
    print("These are my guitars")
    for i, guitar in enumerate (guitars):
        print(f"Guitar {i}: {guitar}")

main()
