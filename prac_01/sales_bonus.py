"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = int(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        users_bonus = sales * 0.1
        print(f"Your bonus is: {users_bonus}")
    else:
        users_bonus = sales * 0.15
        print(f"Your bonus is: {users_bonus}")
    sales = int(input("Enter sales: $"))
# program finishes if the input is a negative number
# "prints the bonus until they enter a negative number."
