# Write a Python program to find if a given string starts with a given
# character using Lambda.
starts_with_char = lambda string, char: string[0] == char

input_string = input("Enter your word: ")
given_char = input("Enter the character to check: ")

result = starts_with_char(input_string, given_char)

if result:
    print(True)
else:
    print(False)
