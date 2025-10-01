"""
CP1404/CP5632 - Practical
Random module functions
"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
- The smallest number that could've been seen is 5, the largest is 19

What did you see on line 2?
- The following numbers: 3, 5, 7, 9

What was the smallest number you could have seen, what was the largest?
- 3 and 9

Could line 2 have produced a 4?
- No as it goes up from 3 in 2s

What did you see on line 3?
- 3.028710060379032, 4.399898636394166

What was the smallest number you could have seen, what was the largest?
- 2.5 and 5.5
"""

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
print(random.randint(1, 100))
