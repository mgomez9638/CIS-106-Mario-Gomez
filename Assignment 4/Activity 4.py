# Activity 4
# The program consists of calculating the areas of shapes.
# The user has to implement the sides of the shapes.
# It all revolves around a single set of answers.

base = float(input("Enter the base: "))
vertical_height = float(input("Enter the vertical height: "))
length_of_sides = float(input("Enter the length of a side: "))
width = float(input("Enter the width: "))
radius = float(input("Enter the radius: "))

area_triangle = (1/2) * base * vertical_height
area_square = length_of_sides ** 2 
area_rectangle = width * vertical_height
area_parallelogram = base * vertical_height
area_trapezoid = (1/2) * (length_of_sides + base)
area_circle = 3.14 * (radius ** 2)

print("The area of the triangle is " + str(area_triangle) + 
      ". The area of a a square is " + str(area_square) + 
      ". The area of rectangle is " + str(area_rectangle) + 
      ". The area of parallelogram is " + str(area_parallelogram) + 
      ". The area of a trapezoid is " + str(area_trapezoid) + 
      ". The area of a circle is " + str(area_circle) + ".")
