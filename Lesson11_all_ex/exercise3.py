#  Write a Python function to return the even numbers from a given list. Sample 
# List
# : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = get_even_numbers(sample_list)

print(result)

