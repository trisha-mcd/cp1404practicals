"""
CP1404/CP5632 Practical
Lottery Ticket Generator
"""
import random

NUMER_OF_ROWS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

amount_of_quick_picks = int(input("How many quick picks? "))
for i in range(amount_of_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMER_OF_ROWS:
        numbers = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(numbers)
    quick_pick.sort()
    formatted_numbers = ' '.join("{:3}".format(num) for num in quick_pick)
    print(formatted_numbers)




