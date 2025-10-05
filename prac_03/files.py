"""
CP1404/CP5632 - Practical
"""

# 1. Asks for users name and writes to file name.txt
name = input("Name: ")
out_file = open("name.txt", "w")  # mode = 'w' which is write
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and greet name
in_file = open("name.txt", "r")  # mode = 'r' which is read
name_from_file = in_file.read().strip()  # .strip() will remove \n
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from number.txt and print sum
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())  # 17
    second_number = int(in_file.readline())  # 42
result = first_number + second_number
print(result)

# 4. Prints the total for all lines in numbers.txt
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)  # converts str into int
        total += number
print(total)
