"""CP1404/CP5632 Practical"""

"""Asks user for 5 numbers and stores into a list"""
numbers = []
for i in range(5): # 5 iterations
    users_number = int(input("Number: "))
    numbers.append(users_number) # adds numbers into list
average = sum(numbers) / len(numbers)
print(f"The first number is {numbers[0]}") # index 0 is the first item in list
print(f"The last number is {numbers[4]}") # index 4 is the last number in list
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")

"""Asks user for username for authorization"""
username = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
person_username = input("Username: ")
if person_username in username:
    print("Access granted")
else:
    print("Access denied")