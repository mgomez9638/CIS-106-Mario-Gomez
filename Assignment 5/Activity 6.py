# Activity 6
# This program is intended to determine how much paint is required to paint a room.
# It, also, expresses how much the gallons of paint cost.

length = float(input("Enter the length of the room(in feet): "))
width = float(input("Enter the width of the room(in feet): "))
height = float(input("Enter the height of the room(in feet): "))
price_per_gallon = float(input("Enter the price per gallon of paint: $"))
square_feet_per_gallon = float(input("Enter the square feet that a gallon of paint will cover: "))

total_area = round(2 * length * height + 2 * width * height, 2)
gallons = int(round(total_area / square_feet_per_gallon + 0.5))
total_price_of_paint = round(gallons * price_per_gallon, 2)

print("The total area of the room is " + str(total_area) + 
      " square feet. The number of gallons needed are " + str(gallons) + 
      ". The total cost of the paint is $" + str(total_price_of_paint) + 
      ".")
