# Write a Python program to square and cube every number in a given list of
# integers using Lambda.
# Sample. ([1,2,3,4,5])
# Output: ([1, 4, 9, 16, 25], [1, 8, 27, 64, 125])
nums = ([1,2,3,4,5])
squared_nums = list(map(lambda x: x**2, nums))
cubed_nums = list(map(lambda x: x**3, nums))
print(squared_nums)
print(cubed_nums)
