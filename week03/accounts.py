# accounts.py
# This program reads 10 characters acc number
# showing only the last 4 digits
# first 6 shows as Xs

# Andrew Andolfo

account = input('Please enter a 10 digit account number: ')
print ('XXXXXX{}' .format(account[-4:]))
# This program is not very reliable because it 
# does not limit the number of characters and 
# allows the user to add too many variables,
# which may cause future issues.

# To solve this issue, several adjustments are needed,
# such as using concepts I'm still learning,
# like While loops, max(), and min()

# I also recommend to limit the allowed characters
# to only numbers, or numbers and letters, etc.