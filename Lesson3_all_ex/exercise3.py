#Write a Python program to remove the n-th index character from a nonempty string.
#Example:
#Sample string: ‘abcdefgh’
#n - 3
#Expected result: abcefgh
test_string = "abcdefgh"
first_letter = test_string[:3] + test_string[4:]
print(first_letter)


