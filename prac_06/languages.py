"""CP1404 - Practical
Creating a class for programming language
Started - Finished: 11:50am -
Estimated time: 50 minutes
Actual time:
 """
from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic",True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(visual_basic)

main()