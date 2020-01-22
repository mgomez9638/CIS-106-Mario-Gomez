#Assignment Three
#This program gives the user access to calculate the distance in U.S. standard lengths. It converts miles into yards, feet, and inches.
print("Enter distance in miles: ")
miles = float(input())
yards = 1760 * miles
feet = 5280 * miles
inches = 63360 * miles 
print("The distance in yards is " + str(yards) + ". The distance in feet is " + str(feet) + ". The distance in inches" + str(inches) + ".", end='',flush=True)
