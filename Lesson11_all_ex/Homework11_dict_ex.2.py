# Write a python program which concat 2 dicts.
def concat_dicts(dict1,dict2):
    result_dict = {**dict1,**dict2}
    return result_dict
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
result = concat_dicts(dict1,dict2)
print(result)