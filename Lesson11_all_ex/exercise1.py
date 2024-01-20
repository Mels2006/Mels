# Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0, 
# 7)Expected Output : 13
def my_sum(numbers):
    result = 0
    for x in numbers:
        result+=x
    return result
print(my_sum([8,2,3,0]))