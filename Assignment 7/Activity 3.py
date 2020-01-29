# Activity 3
# This program gives the user access to determine between either the US measurement system or the metric measurement system.
# It starts with the user implementing the miles and then it branches out to the other measuring lengths. 

def GET_CHOICE():
        choice = input("Enter U to convert US measurements or M to convert metric measurements: ")
        return choice 


def GET_DISTANCE():
        distance = float(input("Enter miles: "))
        return distance 
        

def CALCULATE_YARDS(distance):
        yards = round(distance * 1760 + 0.5 , 2)
        return yards


def CALCULATE_YARDS(distance):
        feet = round(distance * 5280 + 0.5, 2)
        return feet


def CALCUALTE_INCHES(distance):
        inches = round(distance * 63360 + 0.5, 2)
        return inches


def DISPLAY_USMEASUREMENTS(yards, feet, inches):
        print("The distance in yards is " + str(yards) + 
        ". The distance in feet is " + str(feet) + 
        ". The distance in inches is " + str(inches) + 
        ".")


def CALCULATE_KILOMETERS(distance):
        kilometers = round(distance * 1.609 + 0.5, 2)
        return kilometers


def CALCUALTE_METERS(distance):
        meters = round(distance * 1609.344 + 0.5, 2)
        return meters


def CALCULATE_CENTIMETERS(distance):
        centimeters = round(distance * 160934.4 + 0.5, 2)
        return centimeters


def DISPLAY_METRICMEASUREMENTS(kilometers, meters, centimeters):
        print("The distance in kilometers is " + str(kilometers) + 
        ". The distance in meters is " + str(meters) + 
        ". The distance in centimeters is " + str(centimeters) + 
        ".")


# Main
choice = GET_CHOICE()
distance = GET_DISTANCE()
if choice == "U" or choice == "u":
    yards = CALCULATE_YARDS(distance)
    feet = CALCULATE_FEET(distance)
    inches = CALCULATE_INCHES(distance)
    DISPLAY_USMEASUREMENTS(yards, feet, inches)
else:
    if choice == "M" or choice == "m":
        kilometers = CALCULATE_KILOMETERS(distance)
        meters = CALCULATE_METERS(distance)
        centimeters = CALCULATE_CENTIMETERS(distance)
        display_MetricMeasurements(kilometers, meters, centimeters)
    else:
        print("You must enter U to convert to US measurements or M to conver to metric measurements!")
