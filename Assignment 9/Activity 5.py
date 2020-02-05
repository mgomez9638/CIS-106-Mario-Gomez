# Activity 5 from Assignment 7 
# The user determines their sock size by their shoe size. 
# It has a while loop included to determine their sock size and could check other sock sizes.  

                        
def getShoeSize():
    print("Enter your shoe size: ")
    shoeSize = float(input())
    
    return shoeSize

def getSockSize(shoeSize):
    sockSize = int(shoeSize + 0.5)
    
    return sockSize

# Main
shoeSize = getShoeSize()
sockSize = getSockSize(shoeSize)
while True:
    if 0 < sockSize and sockSize < 4:
        print("Your sock size is extra small.")
    else:
        if 4 <= sockSize and sockSize <= 6:
            print("Your sock size is small.")
        else:
            if 7 <= sockSize and sockSize <= 9:
                print("Your sock size is medium.")
            else:
                if 10 <= sockSize and sockSize <= 12:
                    print("Your sock size is large.")
                else:
                    if 13 <= sockSize and sockSize <= 34:
                        print("Your sock size is extra large.")
                    else:
                        print("Please enter a valid shoe size from 1 to 34.")
