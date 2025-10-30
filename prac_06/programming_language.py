"""CP1404 - Practical
Creating a class for programming language
Started - Finished: 11:50am -
Estimated time: 50 minutes
Actual time:
 """

class ProgrammingLanguage:
    def __init__(self, is_dynamic = False, support_reflection = False, year = 0):
        """Initialise programming language,
        typing: Static or Dynamic
        reflection: Yes or No
        Year: int"""
        self.is_dynamic = is_dynamic
        self.support_reflection = support_reflection
        self.year = year
