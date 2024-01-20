#Append new string in the middle of a given (even number of characters) string
#Example:
#Sample = ‘python’
#new_string = ‘new’
#Expected pytnewhon
test_string = "conect"
first_letter = test_string[:3] + 'new' + test_string[-3:]
print(first_letter)

