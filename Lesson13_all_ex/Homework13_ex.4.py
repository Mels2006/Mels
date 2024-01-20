# Write a Python program to find intersection of two given arrays using
# Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

find_intersection = lambda array1, array2: list(filter(lambda x: x in array1, array2))


array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]


intersection = find_intersection(array1, array2)

print(intersection)
