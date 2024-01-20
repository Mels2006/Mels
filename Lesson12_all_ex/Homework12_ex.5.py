# Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.
def sum_of_squares(n):
    sum_result = 0
    for i in range(1, n):
        sum_result += i**2
    return sum_result

n = 5
result = sum_of_squares(n)
print(result)
