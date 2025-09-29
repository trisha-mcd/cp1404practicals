"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from score import determine_score

MENU = """(G)et score
(P)rint result
(S)how star
(Q)uit"""""


def main():
    """This is the main function for score program"""
    score = None
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = get_valid_score()
        elif user_choice == "P":
            if score_is_valid(score):
                result = determine_score(score)  # function from score.py
                print(f"Score: {score}, {result}")
        elif user_choice == "S":
            if score_is_valid(score):
                print("*" * score)
        else:
            print("Invalid")
        print(MENU)
        user_choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get score and validate it"""
    score = int(input("Score:"))
    while score < 0 or score > 100:
        print("Invalid, try again silly goose")
        score = int(input("Score:"))
    return score


def score_is_valid(score):
    """Checking if the score is valid"""
    if score is None:
        print("There is no score silly goose!")
        return False
    return True


main()
