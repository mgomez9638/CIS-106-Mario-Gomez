# Activity 1
# The program consists of the user selecting which shape they would like to calculate.
# All of the shapes are in a class to be easier to work with.
# The user has to implement the sides of the shape.
# It displays the answers at the end.
# Error handling has been included.


import sys


def get_choice():
    choice = input("Please enter one of the following abbreviations: T for triangle, S for square, R for rectangle, P for parallelogram, TR for trapezoid or C for circle: ")
    return choice


def shape_triangle():
    try:
        base = float(input("Enter the base: "))
        vertical_height = float(input("Enter the vertical height: "))
        length_of_sides = 0
        width = 0
        radius = 0
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_square():
    try:
        base = 0
        vertical_height = 0
        length_of_sides = float(input("Enter the length of a side: "))
        width = 0
        radius = 0
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_rectangle():
    try:
        base = 0
        vertical_height = float(input("Enter the vertical height: "))
        length_of_sides = 0
        width = float(input("Enter the width: "))
        radius = 0
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_parallelogram():
    try:
        base = float(input("Enter the base: "))
        vertical_height = float(input("Enter the vertical height: "))
        length_of_sides = 0
        width = 0
        radius = 0
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_trapezoid():
    try:
        base = float(input("Enter the base: "))
        vertical_height = 0
        length_of_sides = float(input("Enter the length of a side: "))
        width = 0
        radius = 0
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


def shape_circle():
    try:
        base = 0
        vertical_height = 0
        length_of_sides = 0
        width = 0
        radius = float(input("Enter the radius: "))
        return base, vertical_height, length_of_sides, width, radius
    except TypeError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])
    except ValueError:
        print("You need to enter a number!")
        print(sys.exc_info()[1])


class shape_area():
    def __init__(self, base, vertical_height, length_of_sides, width, radius):
        self.base = base
        self.vertical_height = vertical_height
        self.length_of_sides = length_of_sides
        self.width = width
        self.radius = radius


    def area_triangle(self):
        return self.base * self.vertical_height * (1/2)


    def area_square(self):
        return self.length_of_sides ** 2


    def area_rectangle(self):
        return self.width * self.vertical_height


    def area_parallelogram(self):
        return self.base * self.vertical_height


    def area_trapezoid(self):
        return (self.length_of_sides + self.base) * (1/2)


    def area_circle(self):
        return (self.radius ** 2) * 3.14


def main():
    print("\t\tWelcome to the Shape Area Program!\n\n")
    choice = get_choice()
    if (choice == "T" or choice == "t"):
        base, vertical_height, length_of_sides, width, radius = shape_triangle()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a triangle is ", round(shape.area_triangle(), 2))
    elif (choice == "S" or choice == "s"):
        base, vertical_height, length_of_sides, width, radius = shape_square()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a square is ", round(shape.area_square(), 2))
    elif (choice == "R" or choice == "r"):
        base, vertical_height, length_of_sides, width, radius = shape_rectangle()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a rectangle is ", round(shape.area_rectangle(), 2))
    elif (choice == "P" or choice == "p"):
        base, vertical_height, length_of_sides, width, radius = shape_parallelogram()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a parallelogram is ", round(shape.area_parallelogram(), 2))
    elif (choice == "Tr" or choice == "tr"):
        base, vertical_height, length_of_sides, width, radius = shape_trapezoid()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a trapezoid is ", round(shape.area_trapezoid(), 2))
    elif (choice == "C" or choice == "c"):
        base, vertical_height, length_of_sides, width, radius = shape_circle()
        shape = shape_area(base, vertical_height, length_of_sides, width, radius)
        print("The area of a circle is ", round(shape.area_circle(), 2))
    else:
        raise Exception("You must enter T for triangle, S for square, R for rectangle, P for parallelogram, TR for trapezoid or C for circle!", sys.exc_info()[1])
    print("\n\n\t\tThank you for using the Shape Area Program!")


main()
