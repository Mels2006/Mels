#Write a Python program to iterate over dictionaries using for loops and print out
#keys and values with f_string
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}


for key, value in sample_dict.items():
    print(f"Key: {key}, Name: {value['name']}, Salary: {value['salary']}")