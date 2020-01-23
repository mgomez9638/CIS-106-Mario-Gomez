# Activity 5
# It gives the user the power to calculate the amount of floor covering required.
# The measurements start at linear feet and converts into square yards.

print("Enter the base(in feet): ")
base = float(input())
print("Enter the height(in feet): ")
height = float(input())

roomAreaInFeet = base * height
roomAreaInYards = roomAreaInFeet / 3

print("The amount of floor required is " + str(roomAreaInYards) + 
      " sq. yds.")
