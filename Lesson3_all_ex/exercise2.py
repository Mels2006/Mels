#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
#Example:
#Sample String : 'abc'
#Expected Result : 'abcing'
#_______________________
#Sample String : 'string'
#Expected Result : 'stringly'
test_string = "fix"
first_letter = test_string[:] + 'ing'
print(first_letter)



