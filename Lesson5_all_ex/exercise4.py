#Write a Python program to find the second smallest number in a list
numbers = [1, 2, 3, 4, 5]
smallest_number = float('inf')
second_smallest_number = float('inf')

for number in numbers:
    if number < smallest_number:
        second_smallest_number = smallest_number
        smallest_number = number
    elif number < second_smallest_number and number != smallest_number:
        second_smallest_number = number

print(second_smallest_number)
