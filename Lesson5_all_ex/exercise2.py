#Write a Python program to get the largest number from a list.
numbers = [1, 44, 3, 4, 7]
largest_number = 0

for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)
