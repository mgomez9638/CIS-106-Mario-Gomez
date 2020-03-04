# Activity 2
# This program implements a text file to be able to read information.
# It displays all the scores from the file.
# The program intents to display the high score, low score, and average score.
# This program includes error handling.


import os
import sys


# check if text file exists
def file_exist():
    try:
        my_file = "scores.txt"
        if os.path.isfile(my_file):
            print("Processing....\n")
            print("File does exist!\n")
            return my_file
    except FileNotFoundError:
        print("File is missing", my_file)
        print(sys.exc_info()[1])


# read the text file
def get_file(my_file):
    try:
        scores = []
        my_file = open("scores.txt", "r")
        my_file.readline()
        for line in my_file:
            try:
                text = line.split(",")
                scores.append(float(text[1]))
            except ValueError:
                print("Incorrect data", my_file)
                print(sys.exc_info()[1])
        my_file.close()
        return scores
    except Exception:
        print("Error reading the format", my_file)
        print(sys.exc_info()[1])
    if not my_file:
        print("File is empty!")


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
    scores = get_file(my_file)
    high = get_high(scores)
    low = get_low(scores)
    average = get_average(scores)
    display_result(high, low, average)
    print("\n\n\t\tThank You for Programming with Files!\n\n")


main()
