#Activty 2 on Flowgorithm
#This activity gives the user access to figure out how old they are by year.
#It displays their age by year, month, day, hours, minutes, and seconds.
print("Enter your age(in years): ")
age = int(input())
months = 12 * age
days = 365 * age
hours = 8760 * age
minutes = 525600 * age
seconds = 31536000 * age
print("You are")
print(age)
print("years old,")
print(months)
print("months old,")
print(days)
print("days old,")
print(hours)
print("hours old,")
print(minutes)
print("minutes old,")
print(seconds)
print("seconds old")

#Activity 2 on Repl.it
#The code layout is different, but it works the same way.
age = int(input("Enter your age(in years): "))
months = 12 * age
days = 365 * age
hours = 8760 * age
minutes = 525600 * age
seconds = 31536000 * age
print("You are", age, "years old,", months, "months old,", days, "days old,", hours, "hours old,", minutes, "minutes old,", seconds, "seconds old" )
