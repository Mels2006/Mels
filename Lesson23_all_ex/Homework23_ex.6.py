# Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore
dict1 = {'_key1': 1, 'key2': 2, 'key3': 3}
dict2 = {'_key4': 4, 'key5': 5, 'key6': 6}

merged_dict = {key: value for key, value in {**dict1, **dict2}.items() if not key[0] == '_'}

print(merged_dict)
