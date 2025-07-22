# imported random library to use its function
import random

# asking user input
ask = input("Do you wish to rool dice for yes type Y for no type N: ")

# adding conditon
if ask == "Y" or ask == "y":
    # used random function wich randomply choose number from 1 to 6 inclusive
    num = random.randint(1,6)
    print(num)

elif ask == "n" or ask == "N":
    print("Canceled")