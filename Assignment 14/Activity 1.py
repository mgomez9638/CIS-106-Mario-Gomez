# Activity 1
# This program implements a text file to be able to read information.
# It displays all the scores from the file.
# The program intents to display the high score, low score, and average score.


import os


# check if text file exists
def file_exist():
    my_file = input("Enter the text file with the extension: ")
    if os.path.isfile(my_file):
        print("\n","Processing....", "\n")
        print("File does exist!", "\n")
    else:
        print("\n", "File does not exist!", "\n")
    return my_file


# read the text file
def get_file(my_file):
    scores = []
    with open(my_file, "r") as txt_file: 
        txt_file.readline()
        for line in txt_file:
            text = line.split(",")
            scores.append(float(text[1]))
    return scores


# user can enter more scores
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
    scores = get_file(my_file)
    scores = get_scores(scores)
    high = get_high(scores)
    low = get_low(scores)
    average = get_average(scores)
    display_result(high, low, average)
    print("\n\n\t\tThank You for Programming with Files!\n\n")


main()
