# Activity 1
# The program consists of the user selecting which shape they would like to calculate.
# All of the shapes are in a class to be easier to work with.
# The user has to implement the sides of the shape.
# It displays the answers at the end.
# Error handling has been included.


import math
import sys


class Shape_Area():
    def area_triangle(self, base, height):
        return base * height / 2


    def area_square(self, length):
        return length ** 2


    def area_rectangle(self, width, height):
        return width * height


    def area_parallelogram(self, base, height):
        return base * height


    def area_trapezoid(self, side, base):
        return (side + base) / 2


    def area_circle(self, radius):
        return math.pi * radius ** 2


def get_choice():
    choice = input("Please enter one of the following abbreviations: T for triangle, S for square, R for rectangle, P for parallelogram, TR for trapezoid or C for circle: ")
    return choice


def shape_triangle():
    try:
        base = float(input("Enter the base: "))
        height = float(input("Enter the vertical height: "))
        shape = Shape_Area()
        area = shape.area_triangle(base, height)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_square():
    try:
        side = float(input("Enter the length of a side: "))
        shape = Shape_Area()
        area = shape.area_square(side)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_rectangle():
    try:
        height = float(input("Enter the vertical height: "))
        width = float(input("Enter the width: "))
        shape = Shape_Area()
        area = shape.area_rectangle(width, height)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_parallelogram():
    try:
        base = float(input("Enter the base: "))
        height = float(input("Enter the vertical height: "))
        shape = Shape_Area()
        area = shape.area_parallelogram(base, height)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_trapezoid():
    try:
        base = float(input("Enter the base: "))
        side = float(input("Enter the length of a side: "))
        shape = Shape_Area()
        area = shape.area_trapezoid(side, base)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_circle():
    try:
        radius = float(input("Enter the radius: "))
        shape = Shape_Area()
        area = shape.area_circle(radius)
        return area
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def main():
    print("\t\tWelcome to the Shape Area Program!\n\n")
    choice = get_choice()
    if (choice == "T" or choice == "t"):
        area = shape_triangle()
        print("The area of a triangle is ", round(area, 2))
    elif (choice == "S" or choice == "s"):
        area = shape_square()
        print("The area of a square is ", round(area, 2))
    elif (choice == "R" or choice == "r"):
        area = shape_rectangle()
        print("The area of a rectangle is ", round(area, 2))
    elif (choice == "P" or choice == "p"):
        area = shape_parallelogram()
        print("The area of a parallelogram is ", round(area, 2))
    elif (choice == "Tr" or choice == "tr"):
        area = shape_trapezoid()
        print("The area of a trapezoid is ", round(area, 2))
    elif (choice == "C" or choice == "c"):
        area = shape_circle()
        print("The area of a circle is ", round(area, 2))
    else:
        raise Exception("You must enter T for triangle, S for square, R for rectangle, P for parallelogram, TR for trapezoid or C for circle!", sys.exc_info()[1])
    print("\n\n\t\tThank you for using the Shape Area Program!")


main()
