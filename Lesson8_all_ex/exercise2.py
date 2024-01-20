#Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500},
}

sample_dict['emp2']['salary'] = 5000
print(sample_dict)