# Write a python function, which add a new value
# with given key in dict.
def add_to_dict(dictionary, key, value):
    dictionary.append((key, value))

my_dict = [('a', 1), ('b', 2), ('c', 3)]
add_to_dict(my_dict, 'd', 4)

print(my_dict)