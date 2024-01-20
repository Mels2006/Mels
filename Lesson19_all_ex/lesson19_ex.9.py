# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary
def find_max_key(dictionary):
    max_key = ""
    max_value = 0

    for key in dictionary:
        value = dictionary[key]
        if value > max_value:
            max_key = key
            max_value = value

    return max_key

my_dict = {'a': 10, 'b': 5, 'c': 10, 'd': 15}
result = find_max_key(my_dict)

print(f"The key with the maximum value is: {result}")


