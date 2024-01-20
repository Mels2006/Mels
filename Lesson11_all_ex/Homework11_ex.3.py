# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


number = int(input("Enter your number: "))
result = factorial(number)


print(result)

