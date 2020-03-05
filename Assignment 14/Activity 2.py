import os
import sys


# check if text file exists
def file_exist():
    my_file = "scores.txt"
    if os.path.isfile(my_file):
        print("Processing....\n")
        print("File does exist!\n")
        return my_file


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
                print("Missing data", my_file)
                print(sys.exc_info()[1])
                pass
            except IndexError:
                print("Incorrectly formatted", my_file)
                print(sys.exc_info()[1])
        my_file.close()
        return scores
    except FileNotFoundError:
        print("Missing file", my_file)
        print(sys.exc_info()[1])


# high score
def get_high(my_file, scores):
    try:
        high = max(scores)
        return high
    except TypeError:
        print("Wrong type", my_file)
        print(sys.exc_info()[1])
        pass
    except ValueError:
        print("Missing data", my_file)
        print(sys.exc_info()[1])
        pass


# low score
def get_low(my_file, scores):
    try:
        low = min(scores)
        return low
    except TypeError:
        print("Wrong type", my_file)
        print(sys.exc_info()[1])
        pass
    except ValueError:
        print("Missing data", my_file)
        print(sys.exc_info()[1])
        pass


# average score
def get_average(my_file, scores):
    try:
        total = sum(scores)
        average = round(total/len(scores), 2)
        return average
    except ZeroDivisionError:
        print("Missing values", my_file)
        print(sys.exc_info()[1])
        pass
    except ValueError:
        print("Missing data", my_file)
        print(sys.exc_info()[1])
        pass
    except TypeError:
        print("Wrong type", my_file)
        print(sys.exc_info()[1])
        pass


# displays scores
def display_result(my_file, high, low, average):
    try:
        print("The highest score is: ", high)
        print("The lowest score is: ", low)
        print("The average score is: ", average)
    except ValueError:
        print("Missing data", my_file)
        print(sys.exc_info()[1])
        pass


# main function
def main():
    print("\t\tWelcome to Programming with Files!\n\n")
    my_file = file_exist()
    scores = get_file(my_file)
    high = get_high(my_file, scores)
    low = get_low(my_file, scores)
    average = get_average(my_file, scores)
    display_result(my_file, high, low, average)
    print("\n\n\t\tThank You for Programming with Files!\n\n")


main()
