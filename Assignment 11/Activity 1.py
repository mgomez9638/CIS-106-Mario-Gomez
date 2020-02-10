# Activity 1 from Static/Fixed-Length Arrays
# This program asks the user to enter grade scores to figure out the average grade score. 
# It displays the total points, highest score enter, lowest score entered and the average grade score.


def get_size():
    size = input("How many score(s) will you be entering today? ")
    return size


def get_scores(size):
    test_scores = []
    for scores in range(int(size)):
        score = input("Enter score: ")
        test_scores.append(float(score))
    return test_scores


def get_total(test_scores):
    total = sum(test_scores)
    return total


def get_maximum(test_scores):
    maximum = max(test_scores)
    return maximum


def get_minimum(test_scores):
    minimum = min(test_scores)
    return minimum


def get_average(test_scores, total):
    average = round(total/len(test_scores), 2)
    return average


def display_result(total, test_scores, average):
    print("The total points entered are: ", total)
    print("The highest score is: ", maximum)
    print("The lowest score is: ", minimum)
    print("The average score is: ", average)


def main():
    size = get_size()
    test_scores = get_scores(size)
    total = get_total(test_scores)
    average = get_average(test_scores, total)
    display_result(total, test_scores, average)


main()
