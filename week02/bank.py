# bank.py
# This program reads 2 float numbers input and prints their sum.
# The number have to be in cent to avoid 
amount1 = int(input("Enter amount 1 (in cent):"))
amount2 = int(input("Enter amount 2 (in cent):"))

# Output formatted to 2 decimal places with Deepseek's help 
print ("The sum of these is €{:.2f}".format((amount1 + amount2)/100))