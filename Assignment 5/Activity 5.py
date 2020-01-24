# Activity 5
# It gives the user the power to calculate the amount of floor covering required.
# The measurements start at linear feet and converts into square yards.

def calculateRoomAreaInFeet(base, height):
    roomAreaInFeet = base * height
    
    return roomAreaInFeet

def calculateRoomAreaInYards(roomAreaInFeet):
    roomAreaInYards = roomAreaInFeet / 3
    
    return roomAreaInYards

def displayResult(roomAreaInFeet, roomAreaInYards):
    print("The amount of floor required is " + str(roomAreaInYards) + " square yards.")

def getBase():
    print("Enter the base(in feet): ")
    base = float(input())
    
    return base

def getHeight():
    print("Enter the height(in feet): ")
    height = float(input())
    
    return height

# Main
base = getBase()
height = getHeight()
roomAreaInFeet = calculateRoomAreaInFeet(base, height)
roomAreaInYards = calculateRoomAreaInYards(roomAreaInFeet)
displayResult(roomAreaInFeet, roomAreaInYards)
