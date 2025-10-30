"""CP1404 - Practical
Creating a class for programming language
Started - Finished: 11:50am - 1:06pm
Estimated time: 50 minutes
Actual time: 1hr 16 mins
 """


class ProgrammingLanguage:
    """Represent Programming Languages"""
    def __init__(self, name="", typing="Dynamic", support_reflection=False, year=0):
        """Store programming language values,
        typing: Static or Dynamic
        reflection: Yes or No
        Year: int"""
        self.name = name
        self.typing = typing
        self.support_reflection = support_reflection
        self.year = year

    def is_dynamic(self):
        """Return True if typing is dynamic"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string format"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.support_reflection}, First appeared in {self.year}"
