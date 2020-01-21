print("Enter your age(in years): ")
age = int(input())
months = 12 * age
days = 365 * age
hours = 8760 * age
minutes = 525600 * age
seconds = 31536000 * age
print("You are " + str(age) + "years old, " + str(months) + " months old, " + str(days) + " days old, " + str(hours) + " hours old, " + str(minutes) + "minutes old, " + str(seconds) + " seconds old.")
