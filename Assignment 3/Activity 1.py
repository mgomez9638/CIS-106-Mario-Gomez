#Assignment One in Flowgorithm
#This program gives the user access to figure out how much they make weekly, monthly, and annually. 
print("Enter hours worked: ")
hours = int(input())
print("Enter hourly rate: ")
rate = int(input())
weekly = rate * hours
annually = 52 * weekly
monthly = float(annually) / 12
print("Your weekly earnings are $ ")
print(weekly)
print("Your monthly earnings are $ ")
print(monthly)
print("Your annual earnings are $ ")
print(annually)

#Assignment One in Repl.it 
#The layout is a bit different, but it accomplishes the goal.
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
weekly = rate * hours
annually = weekly * 52
monthly = annually / 12
print("Your weekly earnings are $", weekly, "your monthly earnings are $", monthly, "your annual earnings are $", annually)
