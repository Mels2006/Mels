# Write a list comprehension to print this output 
# * 
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
list_1 = "\n".join("".join("*" for j in range(1, i + 1)) for i in range(1, 10))
print(list_1)