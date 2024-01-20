# Write a Python program to get a string made of the first 2 and the last 2 chars from a
# given string.
# Example:
# Sample String : 'w3resource'
# Expected Result : 'w3ce
test_string = "function"
first_letter = test_string[0:2] + test_string[-2:]
print(first_letter)
