# Activity 3
# This program gives the user access to determine between either the US measurement system or the metric measurement system.
# It starts with the user implementing the miles and then it branches out to the other measuring lengths. 


def get_choice():
        print("Welcome to the Measurements Program!")
        choice = input("Enter U to convert to US measurements or M to convert to metric measurements: ")
        return choice 


def get_distance():
        distance = float(input("Enter a distance in miles: "))
        return distance 
        

def calculate_yards(distance):
        yards = round(distance * 1760 + 0.5, 2)
        return yards


def calculate_feet(distance):
        feet = round(distance * 5280 + 0.5, 2)
        return feet


def calculate_inches(distance):
        inches = round(distance * 63360 + 0.5, 2)
        return inches


def display_usmeasurements(yards, feet, inches):
        print("The distance in yards is " + str(yards) + 
        ". \nThe distance in feet is " + str(feet) + 
        ". \nThe distance in inches is " + str(inches) + 
        ". \nThank you for using the Measurements Program!")


def calculate_kilometers(distance):
        kilometers = round(distance * 1.609 + 0.5, 2)
        return kilometers


def calculate_meters(distance):
        meters = round(distance * 1609.344 + 0.5, 2)
        return meters


def calculate_centimeters(distance):
        centimeters = round(distance * 160934.4 + 0.5, 2)
        return centimeters


def display_metricmeasurements(kilometers, meters, centimeters):
        print("The distance in kilometers is " + str(kilometers) + 
        ". \nThe distance in meters is " + str(meters) + 
        ". \nThe distance in centimeters is " + str(centimeters) + 
        ". \nThank you for using the Measurements Program!")


def main():
        choice = get_choice()
        if (choice == "U" or choice == "u"):
            distance = get_distance()
            yards = calculate_yards(distance)
            feet = calculate_feet(distance)
            inches = calculate_inches(distance)
            display_usmeasurements(yards, feet, inches)
        elif (choice == "M" or choice == "m"):
            distance = get_distance()
            kilometers = calculate_kilometers(distance)
            meters = calculate_meters(distance)
            centimeters = calculate_centimeters(distance)
            display_metricmeasurements(kilometers, meters, centimeters)
        else:
            print("You must enter U to convert to US measurements or M to conver to metric measurements!")

main()
