# Activity 6
# This program is intended to determine how much paint is required to paint a room.
# It, also, expresses how much the gallons of paint cost.

def get_length():
      length = float(input("Enter the length of the room(in feet): "))
      return length


def get_width():
      width = float(input("Enter the width of the room(in feet): "))
      return width


def get_height():
      height = float(input("Enter the height of the room(in feet): "))
      return height


def get_price_per_gallon():
      price_per_gallon = float(input("Enter the price per gallon of paint: $"))
      return price_per_gallon


def get_square_feet_per_gallon():
      square_feet_per_gallon = float(input("Enter the square feet that a gallon of paint will cover: "))
      return square_feet_per_gallon


def calculate_total_area(length, width, height):
      total_area = round(2 * length * height + 2 * width * height, 2)
      return total_area


def calculate_gallons(total_area, square_feet_per_gallon):
      gallons = int(round(total_area / square_feet_per_gallon + 0.5))
      return gallons


def calculate_total_price_of_paint(gallons, price_per_gallon):
      total_price_of_paint = round(gallons * price_per_gallon, 2)
      return total_price_of_paint


def display_result(total_area, gallons, total_price_of_paint):
      print("The total area of the room is " + str(total_area) + 
      " square feet. The number of gallons needed are " + str(gallons) + 
      ". The total cost of the paint is $" + str(total_price_of_paint) + 
      ".")

      
def main():
      length = get_length()
      width = get_width()
      height = get_height()
      price_per_gallon = get_price_per_gallon()
      square_feet_per_gallon = get_square_feet_per_gallon()
      total_area = calculate_total_area(length, width, height)
      gallons = calculate_gallons(total_area, square_feet_per_gallon)
      total_price_of_paint = calculate_total_price_of_paint(gallons, price_per_gallon)
      display_result(total_area, gallons, total_price_of_paint)

      
main()
