# Activity 1 from Assignment 3 
# This program gives the user access to figure out how much they make weekly, monthly, and annually.
# The user has the option to run the amount of money they would be making with different hourly rates.

           
def getExpressions():
    print("Enter the number of expressions: ")
    expressions = int(input())
    
    return expressions

def getValue():
    print("Enter a value: ")
    value = int(input())
    
    return value

# Main
value = getValue()
expressions = getExpressions()
multiplierValue = 1
for multiplierValue in range(1, expressions + 1, 1):
    total = value * multiplierValue
    print(str(value) + " * " + str(multiplierValue) + " = " + str(total))
    multiplierValue = multiplierValue + 1
