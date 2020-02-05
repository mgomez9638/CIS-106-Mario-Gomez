# Activity 2 from For Loops
# This program is made to figure out the average grade scores from the grades that are being enter. 
# The user gets asked how many score(s) they will be entering before the function begins to process the total and average. 


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


def get_average(test_scores, total):
    average = round(total/len(test_scores), 2)
    return average


def main():
    size = get_size()
    test_scores = get_scores(size)
    total = get_total(test_scores)
    average = get_average(test_scores, total)
    print("The total points entered are: ", total)
    print("The average score is: ", average)


main()
