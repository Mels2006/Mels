# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop.
current_number = 1
even_sum = 0


while current_number <= 100:
    if current_number % 2 == 0:
        even_sum += current_number

    current_number += 1

print(f"The sum of even numbers between 1 and 100 is: {even_sum}")