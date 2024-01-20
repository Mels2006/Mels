# Write a Python program to check whether a given string is number or
# not using Lambda.
is_number = lambda s: s.isdigit()

input_string = input("Enter a string to check if it's a number: ")

result = is_number(input_string)

if result:
    print(True)
else:
    print(False)
