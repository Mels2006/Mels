#Check if a value exists in a dictionary
y = 'the pure'
result = False
knights = {'galland': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    if y == v:
        result = True
print(result)