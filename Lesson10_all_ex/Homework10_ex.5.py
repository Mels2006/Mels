# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones
n = int(input("Enter a number (n): "))

fibonacci_sequence = [0, 1]
i = 2

while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)
    i += 1

print("Fibonacci sequence up to", n, ":", fibonacci_sequence)
