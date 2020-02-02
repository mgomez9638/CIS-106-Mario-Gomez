# Activity 1
# This program gives the user access to create a multiplication table.
# You simply begin with entering a value, entering a starting point, and the size of the table.

def getMultiplierValue():
    print("Enter the starting point value: ")
    multiplierValue = int(input())
    
    return multiplierValue

def getSize():
    print("Enter the size of the table(larger than the value): ")
    size = int(input())
    
    return size

def getStableValue():
    print("Enter a value: ")
    stableValue = int(input())
    
    return stableValue

# Main
stableValue = getStableValue()
multiplierValue = getMultiplierValue()
size = getSize()
while stableValue <= size:
    while multiplierValue <= size:
        total = stableValue * multiplierValue
        print(str(stableValue) + " * " + str(multiplierValue) + " = " + str(total))
        multiplierValue = multiplierValue + 1
stableValue = stableValue + 1
