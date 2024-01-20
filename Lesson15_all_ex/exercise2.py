# Write a python function which will get a number and check is 
# your number great or equal the random number of computer 
# (10-100)if yes print True otherwise False.
import random
def check_number_equal(num):
    if num >= random.randint(10,100):
        return True
    else:
        return False
print(check_number_equal(56))