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


def get_reverse(string):
    reverse = "".join(reversed(string))
    return reverse


def display_result(reverse):
    print(reverse)


def main():
    string = get_string()
    reverse = get_reverse(string)
    display_result(reverse)


main()
