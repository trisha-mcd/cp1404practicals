"""CP1404 - Practical
Creating a class for guitars
Started - Finished: 2:00pm - 2:30pm
Estimated time: 50 minutes
Actual time: 30 mins + 10 mins to adjust for guitar_test
 """
YEAR = 2022


class Guitar:
    """Represent Guitar"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise guitar values"""
        self.name = name
        self.year = year
        self.cost = cost

    # def __str__(self):
    #     """Return values into string format"""
    #     return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __str__(self):
        """Return values into string format, for guitar_test output"""
        return f"{self.name} ({self.year}), worth ${self.cost:.2f} {self.is_vintage()}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        age = YEAR - self.year
        return age

        # def is_vintage(self):
        #     """Returns True if the guitar is 50 or more years old"""
        #     # if self.get_age() >= 50:
        #     #     return True
        #     # else:
        #     #     return False

    def is_vintage(self):
        """Returns (vintage) if the guitar is 50 or more years old, for guitar_test output"""
        if self.get_age() >= 50:
            is_vintage_string = "(vintage)"
        else:
            is_vintage_string = ""
        return f"{is_vintage_string}"
