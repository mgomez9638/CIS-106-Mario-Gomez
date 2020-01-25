# Activity 1
# This program helps the user figure out how much money they make.
# The end results include weekly, monthly, and annually before taxes.


def get_hours():
        hours = float(input("Enter hours worked: "))
        return hours


def get_rate():
        rate = float(input("Enter hourly rate: "))
        return rate


def calculate_weekly_rate(hours, rate):
        weekly_rate = round(rate * hours, 2)
        return weekly_rate


def calculate_annually_rate(weekly):
        annually_rate = float(weekly) * 52
        return annually_rate


def calculate_monthly_rate(annually):
        monthly_rate = float(annually) / 12
        return monthly_rate


def display_result(weekly_rate, monthly_rate, annually_rate):
        print("Your weekly_rate earnings are $", weekly_rate, 
              ". Your monthly earnings are $", monthly_rate, 
              ". Your annual earnings are $", annually_rate, 
              ".")


def main():
        hours = get_hours()
        rate = get_rate()
        weekly_rate = calculate_weekly_rate(hours, rate)
        annually_rate = calculate_annually_rate(weekly_rate)
        monthly_rate = calculate_monthly_rate(annually_rate)
        display_result(weekly_rate, monthly_rate, annually_rate)


main()
