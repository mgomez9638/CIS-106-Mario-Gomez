# Activity 1 from Nested Loops
# It is multiplication chart that the user has access to customize.
# The user has access to change the starting point and the ending point.


def get_start():
    start = int(input("Enter the starting multiplied number(Must be smaller than the multiplication chart): ")) 
    return start


def get_size():
    size = int(input("What size multiplication chart would you like? "))
    return size 


def main():
    size = get_size()
    start = get_start()
    print()
    column_string = " "
    for column in range(start, size + 1):
        column_string = column_string + "\t" + str(column)
    print(column_string)
    for row in range(start, size + 1):
        row_string = str(row)
        for column in range(start, size + 1):
            row_string = row_string + "\t" + str(row * column)
            if (row * column) % 2 == 0:
                row_string = row_string + " "
        print(row_string)


main()
