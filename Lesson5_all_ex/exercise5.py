# Write a Python program to remove duplicates from a list
numbers = [5, 6, 78, 14, 5, 2, 6, 78, 15]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
