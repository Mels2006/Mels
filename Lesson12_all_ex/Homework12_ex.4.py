# Find Index Function
# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.
def find_element_index(list, element):
    if element in list:
        return list.index(element)

my_list = [1, 2, 4, 5, 6, 8]
element_to_find = 4
index_result = find_element_index(my_list, element_to_find)

if index_result != -1:
    print(index_result)
