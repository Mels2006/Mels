# 5. Math Operations Exercise:
# Write a function that calculates the square root of a number using the math module.
def the_square_root(number):
    import math
    square_root = math.sqrt(number)
    square_of_square_root = square_root ** 2
    print(f"The square of the square root is: {square_of_square_root}")    
the_square_root(16)
