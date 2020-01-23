print("Enter the base(in feet): ")
base = float(input())
print("Enter the height(in feet): ")
height = float(input())
roomAreaInFeet = base * height
roomAreaInYards = roomAreaInFeet / 3
print("The amount of floor required is " + str(roomAreaInYards) + " sq. yds.")
