# 4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)
def find_common_elements(list_a, list_b):
    common_elements = []

    for num_1 in list_a:
        for num_2 in list_b:
            if num_1 == num_2 and num_1 not in common_elements:
                common_elements.append(num_1)

    return common_elements


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common_elements_result = find_common_elements(list_a, list_b)

print(f"{common_elements_result}")
