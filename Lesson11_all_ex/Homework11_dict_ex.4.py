# Write a python function which create dict from 2
# lists with the same length
def create_dict_from_lists(keys, values):
    result_dict = {}
    for i in range(len(keys)):
        result_dict [keys[i]] = values[i]
    return result_dict

keys_list = ['a', 'b', 'c',]
values_list = [1, 2, 3,]

result_dict = create_dict_from_lists(keys_list, values_list)
print(result_dict)