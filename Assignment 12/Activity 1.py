# Activity 1 from Dynamic Arrays / Lists
# This program asks the user to enter grade scores to figure out the average grade score.
# It displays the total points, highest score entered, lowest score entered, the average grade score, and the  letter grade.


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


def get_maximum(test_scores):
    maximum = max(test_scores)
    return maximum


def get_minimum(test_scores):
    minimum = min(test_scores)
    return minimum


def get_average(test_scores, total):
    average = round(total/len(test_scores), 2)
    return average


def get_letter_grade(average):
    if 90 <= average:
        return "A"
    elif 80 <= average:
        return "B"
    elif 70 <= average:
        return "C"
    elif 60 <= average:
        return "D"
    else:
        return "F"


def display_result(total, test_scores, maximum, minimum, average, letter_grade):
    print("The total points entered are: ", total)
    print("The highest score is: ", maximum)
    print("The lowest score is: ", minimum)
    print("The average score is: ", average)
    print("The letter grade is: ", letter_grade)


def main():
    test_scores = get_scores()
    total = get_total(test_scores)
    maximum = get_maximum(test_scores)
    minimum = get_minimum(test_scores)
    average = get_average(test_scores, total)
    letter_grade = get_letter_grade(average)
    display_result(total, test_scores, maximum, minimum, average, letter_grade)

    
main()
