# Using dict comprehension and a conditional argument create a dictionary from the current
# dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
dict_1 = {"NFLX":4950,"TREX":2400,"XPO":1700,"FIZZ":1800}
dict_2 = {k:v for k,v in dict_1.items() if v > 2000}
print(dict_2)