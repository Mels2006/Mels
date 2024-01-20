# Average Function
# Write a function that calculates the average of a list of numbers.
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5, 6, 7]
average_result = int(calculate_average(my_list))
print(average_result)