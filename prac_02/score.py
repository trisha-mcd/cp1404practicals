"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """This is the main function for score program"""
    score = random.randint(0, 100)
    result = determine_score(score)
    print(f"Score: {score}, {result}")


def determine_score(score):
    """Determine result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__": # only run the entire program if this file is being run directly
    main()
