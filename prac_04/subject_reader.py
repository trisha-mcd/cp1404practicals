"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_infile = read_data_infile(FILENAME)
    print(data_infile)
    print_subject_details(data_infile)


def read_data_infile(filename=FILENAME):
    """Read data_infile from file formatted like: subject,lecturer,number of students."""
    data_infile = []
    with open(filename) as input_file:  # open and close file
        for line in input_file:
            print(line)  # See what a line looks like
            print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            print(parts)  # See if that worked
            print("----------")
            data_infile.append(parts) # creating nestled list, parts list within data list
    return data_infile



def print_subject_details(data_infile: list):
    """Print data from nested list"""
    for subject_details in data_infile:
        print(f"{subject_details[0]} is taught by {subject_details[1]} and {subject_details[2]} students")


main()
