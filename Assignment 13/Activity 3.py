# Activity 3
# This program gives the user access to display there entered elements in vertical form. 


def get_elements():
    elements = input("Enter comma separated elements: \n").split(",")
    elements = "\n".join(elements)
    elements = elements.replace(" ","")
    return elements


def display_result(elements):
    print(elements)


def main():
    elements = get_elements()
    display_result(elements)


main()
