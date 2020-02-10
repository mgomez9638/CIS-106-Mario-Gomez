# Activity 3
# This program asks the user for their birthday to display the weekday they were born on.
# https://en.wikipedia.org/wiki/Zeller%27s_congruence


def get_birthday():
    month, day, year = input("What is your date of birth(mm/dd/yyyy)? ").split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    return month, day, year


def day_of_the_week(weekday):
    if weekday == 0:
        return "Saturday"
    if weekday == 1:
        return "Sunday"
    if weekday == 2:
        return "Monday"
    if weekday == 3:
        return "Tuesday"
    if weekday == 4:
        return "Wednesday"
    if weekday == 5:
        return "Thursday"
    if weekday == 6:
        return "Friday"


def calculate_zeller_congruence(month, day, year):
    if month == 1:
        month = 13
        year -= 1
    if month == 2:
        month = 14
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    weekday = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    weekday = weekday % 7
    print(day_of_the_week(weekday))


def main():
    month, day, year = get_birthday()
    calculate_zeller_congruence(month, day, year)


main()
