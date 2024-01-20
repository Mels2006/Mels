# Generate a list with list comprehension which contains all numbers from (1 - 999)
# ○ Write a list comprehension which iterates on generated list and generate new list where are cubs of odd numbers from first list
lst = [i for i in range(1,999)]
lst_1 = [i**3 for i in lst if i % 2 == 1]
print(lst_1)