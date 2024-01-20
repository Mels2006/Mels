# Write a Python function to check whether a number is in a given range.
def my_function(number, range_start, range_end):
    result = False
    for x in range(range_start, range_end):
        if x == number:
            result = True
            break  
    return result

nuumber_to_check = 5
range_start = 2
range_end = 8

print(my_function(nuumber_to_check, range_start, range_end))

