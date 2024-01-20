# Display the numbers from 1 to 10 except 6.
# Expected Output: 1 2 3 4 5 7 8 9 10
i = 0
while i < 10:
    i +=1
    if i == 6:
        continue
    print(i)