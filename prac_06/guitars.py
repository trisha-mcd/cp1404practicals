"""CP1404 - Practical
Creating a class for guitars
Started - Finished: 2:27pm - 4:00pm
Estimated time: 40mins
Actual time: 2 hrs
 """
from prac_06.guitar import Guitar


def main():
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
    print("... snip ...\n")
    print("These are my guitars")
    for i, guitar in enumerate(guitars):
        print(f"Guitar {i}: {guitar}")


main()
