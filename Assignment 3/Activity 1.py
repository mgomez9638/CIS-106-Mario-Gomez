#Assignment One in Flowgorithm
#This program gives the user access to figure out how much they make weekly, monthly, and annually. 
print("Enter hours worked: ")
hours = float(input())
print("Enter hourly rate: ")
rate = float(input())
weekly = rate * hours
annually = 52 * weekly
monthly = annually / 12
print("Your weekly earnings are $" + str(weekly) + ".Your monthly earnings are $" + str(monthly) + ".Your annually earnings are $" + str(annually) + ".", end='', flush=True)
