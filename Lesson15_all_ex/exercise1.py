# Write a python program which will check is your number equal 
# the random number of computer (1-10)if yes print True otherwise 
# False.
import random

def check_number_equal(num):
    if num == random.randint(1,10):
        return True
    else:
        return False
print(check_number_equal(7))
