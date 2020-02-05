# Activity 1
# This program asks the user to enter grade scores to figure out the average grade score. 
# It displays the total points and average grade score.

def get_scores():
    test_scores = []
    while True:
        try:
            score = float(input("Enter a score(press enter to exit): "))
        except ValueError:
            break
        test_scores.append(score)
    return test_scores


def get_total(test_scores):
    total = sum(test_scores)
    return total


def get_average(test_scores, total):
    average = round(total/len(test_scores), 2)
    return average


def main():
    test_scores = get_scores()
    total = get_total(test_scores)
    average = get_average(test_scores, total)
    print("The total points entered are: ", total)
    print("The average score is: ", average)


main()
