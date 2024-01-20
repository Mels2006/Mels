# Get the same items in two ranges using
# nested loop.(0, 10), (5,15)
list_1 = []
for i in range(0,11):
    for j in range(5, 15):
        if i == j:
            list_1.append(i)
print(list_1)
