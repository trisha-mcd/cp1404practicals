for i in range(1, 21, 2):  # starts at 1, ends at 21, increase by 2
    print(i, end=' ')  # prints i with a space after
print()

"""
a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
"""
for i in range(0, 110, 10):
    print(i, end=' ')
print()

"""
b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
c. print a number of stars.
Ask the user for a number, then print that many stars (*), all on one line.
"""

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")  # end="" prints all on one line

"""
d. print lines of increasing stars.
Ask the user for a number of lines, then print lines of increasing stars, starting at 1 with no blank line.
"""

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):  # starts at 1, inclusive to number of stars (wants 4, gets 4)
    print("*" * i)  # increases the stars pre line till number_of_stars
