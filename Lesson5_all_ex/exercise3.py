#Write a Python program to get the smallest number from a list.
numbers = [6, 2, 3, 4, 5]
smallest_number = 0

for number in numbers:
    if smallest_number == 0 or number < smallest_number:
        smallest_number = number

print(smallest_number)

