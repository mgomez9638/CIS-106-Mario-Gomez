# Activity 5
# The user determines their sock size by their shoe size. 

def calculatesockSize(shoeSize):
    sockSize = int(shoeSize + 0.5)
    
    return sockSize

def getShoeSize():
    print("Enter your shoe size: ")
    shoeSize = float(input())
    
    return shoeSize

# Main
shoeSize = getShoeSize()
sockSize = calculatesockSize(shoeSize)
if sockSize < 4:
    print("Your sock size is extra small.")
else:
    if 4 <= sockSize and sockSize <= 6:
        print("You sock size is small.")
    else:
        if 7 <= sockSize and sockSize <= 9:
            print("Your sock size is medium.")
        else:
            if 10 <= sockSize and sockSize <= 12:
                print("You sock size is large.")
            else:
                print("Your sock size is extra large.")
