# Assignment Two
# This activity gives the user access to figure out how old they are by years, months, days, hours, minutes, and seconds.


def get_age():
        age = int(input("Enter your age(in year): "))
        return age


def calculate_months(age):
        months = 12 * age
        return months

  
def calculate_days(age):
        days = 365 * age
        return days


def calculate_hours(age):
        hours = 8760 * age
        return hours


def calculate_minutes(age):
        minutes = 525600 * age
        return minutes


def calculate_seconds(age):
        seconds = 31536000 * age 
        return seconds 


def display_result(age, months, days, hours, minutes, seconds):
        print("You are", age, "years old,", months, "months old,", days, "days old,", hours, "hours old,", minutes, "minutes old,", seconds, "seconds old.")


def main():
        age = get_age()
        months = calculate_months(age)
        days = calculate_days(age)
        hours = calculate_hours(age)
        minutes = calculate_minutes(age)
        seconds = calculate_seconds(age)
        display_result(age, months, days, hours, minutes, seconds)


main()
