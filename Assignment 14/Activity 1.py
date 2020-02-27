# Activity 1
# This program implements a text file to be able to read information.
# It displays all the scores from the file.
# The program intents to display the high score, low score, and average score.


import os


def file_exist():
    my_file = input("Enter the text file with the extension: ")
    if os.path.isfile(my_file):
        print("Processing....", "\n")
        print("File does exist!", "\n")
    else:
        print("File does not exist!", "\n")
    return my_file


def get_file(my_file):
    names = []
    scores = []
    my_file = open("scores.txt", "r")
    my_file.readline()
    for line in my_file:
        text = line.split(",")
        names.append(text[0])
        scores.append(float(text[1]))
    my_file.close()
    return names, scores


def get_scores(scores):
    while True:
        try:
            more_scores = float(input("Enter a score(press enter to exit): "))
        except ValueError:
            break
        scores.append(more_scores)
    print(scores)
    return scores


# high score
def get_high(scores):
    high = max(scores)
    return high


# low score
def get_low(scores):
    low = min(scores)
    return low


# average score
def get_average(scores):
    total = sum(scores)
    average = round(total/len(scores), 2)
    return average


# displays scores
def display_result(high, low, average):
    print("The highest score is: ", high)
    print("The lowest score is: ", low)
    print("The average score is: ", average)


# main function
def main():
    print("\t\tWelcome to Programming with Files!\n\n")
    my_file = file_exist()
    names, scores = get_file(my_file)
    scores = get_scores(scores)
    high = get_high(scores)
    low = get_low(scores)
    average = get_average(scores)
    display_result(high, low, average)
    print("\n\n\t\tThank You for Programming with Files!\n\n")


main()
