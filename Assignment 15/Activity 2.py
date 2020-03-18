# Assignment Two
# This activity gives the user access to figure out how old they are by years, months, days, hours, minutes, or seconds.


import sys


def get_choice():
        choice = input("Please enter one of the following abbreviations: M for months, D for days, H for hours, MI for minutes or S for seconds: ")
        return choice


class age_converter():
    _age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = int(age)

    def __init__(self, age=None):
        if age <= 0:
            raise ValueError("Your age cannot be negative.", sys.exc_info()[1])
        elif age is not None:
            self._age = age

    def months(self):
        return self.age * 12

    def days(self):
        return self.age * 365

    def hours(self):
        return self.age * 8760

    def minutes(self):
        return self.age * 525600

    def seconds(self):
        return self.age * 3153600


def main():
    choice = get_choice()
    if (choice == "M" or choice == "m"):
        years = age_converter(age=int(input("Enter your age(in year(s)): ")))
        print("If you are ", years.age, " years old, then you are ", years.months(), " months old.")
    elif (choice == "D" or choice == "d"):
        years = age_converter(age=int(input("Enter your age(in year(s)): ")))
        print("If you are ", years.age, " years old, then you are ", years.days(), " days old.")
    elif (choice == "H" or choice == "h"):
        years = age_converter(age=int(input("Enter your age(in year(s)): ")))
        print("If you are ", years.age, " years old, then you are ", years.hours(), " hours old.")
    elif (choice == "MI" or choice == "Mi" or choice == "mi"):
        years = age_converter(age=int(input("Enter your age(in year(s)): ")))
        print("If you are ", years.age, " years old, then you are ", years.minutes(), " hours old.")
    elif (choice == "S" or choice == "s"):
        years = age_converter(age=int(input("Enter your age(in year(s)): ")))
        print("If you are ", years.age, " years old, then you are ", years.seconds(), " seconds old.")
    else:
        raise Exception("You must enter M for months, D for days, H for hours, MI for minutes or S for seconds!", sys.exc_info()[1])


main()
