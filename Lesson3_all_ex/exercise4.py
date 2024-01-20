#Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged.
#Example:
#Sample: ‘abcdefgh’
#Expected: ‘hbcdefga’
test_string = "alphabet"
first_letter = test_string[-1:] + test_string[1:-1] + test_string[0]
print(first_letter)






