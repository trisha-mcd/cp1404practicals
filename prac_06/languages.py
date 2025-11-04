"""CP1404 - Practical
Creating a class for programming language
Started - Finished: 11:50am - 1:06pm
Estimated time: 50 minutes
Actual time: 1hr 16 mins
 """
from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic",True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    programming_languages = [python, ruby, visual_basic] # a list containing 3 separate ProgrammingLanguage objects
    print("The dynamically typed languages are:")
    for langauge in programming_languages:
        if langauge.is_dynamic():
            print(langauge.name)
main()