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
