# Activity 2
# This program asks the user to enter grade scores to figure out the average grade score. 
# It displays the average grade score and letter grade.


def get_scores():
    test_scores = []
    while True:
        score = float(input("Enter a score(enter a negative integer): "))
        if score < 0: 
            break
        test_scores.append(score)
    return test_scores


def get_total(test_scores):
    total = sum(test_scores)
    return total


def get_average(test_scores, total):
    average = round(total/len(test_scores) + .005, 2)
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


def main():
    test_scores = get_scores()
    total = get_total(test_scores)
    average = get_average(test_scores, total)
    letter_grade = get_letter_grade(average)
    print("The total points entered are: ", total)
    print("The average score is: ", average)
    print("The letter grade is: ", letter_grade)

    
main()
