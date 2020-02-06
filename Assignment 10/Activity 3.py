# Activity 1 from Assignment 3 
# This program gives the user access to figure out how much they make weekly, monthly, and annually.
# The user has the option to run the amount of money they would be making with different hourly rates.


def getAnotherGo():
    print("Would you like to go again? ")
    anotherGo = input()
    
    return anotherGo

def getHours():
    print("Enter hours worked: ")
    hours = float(input())
    
    return hours

def getRate():
    print("Enter hourly rate of pay: ")
    rate = float(input())
    
    return rate

# Main
pay = True
while pay == True:
    hours = getHours()
    rate = getRate()
    weekly = rate * hours
    annually = 52 * weekly
    monthly = annually / 12
    print("This pay is before taxes. Your weekly earnings are $" + str(weekly) + ". Your monthly earnings are $" + str(monthly) + ". Your annually earnings are $" + str(annually) + ".")
    goAgain = True
    while goAgain == True:
        anotherGo = getAnotherGo()
        if anotherGo == "yes" and anotherGo == "Yes" and anotherGo == "y" and anotherGo == "Y":
            goAgain = True
        else:
            goAgain = False
