# Count how many even and odd numbers
# are in given range (10,35).
even = 0
odd = 0
for i in range(10,35):
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print(odd,even)