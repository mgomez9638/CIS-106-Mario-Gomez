# Activity 2
# This program asks the user to enter a sentence.
# It displays the sentence in reverse letter by letter.


def get_string():
    string = input("Write a sentence: \n")
    string = string.split(" ")
    while "" in string:
        string.remove("")
    string = " ".join(string)
    return string


def display_result(string):
    print(string[::-1])


def main():
    string = get_string()
    display_result(string)


main()
