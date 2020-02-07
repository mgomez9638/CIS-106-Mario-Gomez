# Activity 1 from For Loops
# This program gives the user access to create a multiplication table.
# You simply begin with entering a value, entering a starting point, and the size of the table.
           
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
