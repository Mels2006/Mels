# Sum of Digits
# Write a Python program that takes a positive integer as input and calculates the sum
# of its digits. For example, if the input is 12345, the output should be 15 (1 + 2 + 3 + 4
# + 5 = 15). Use a while loop to perform this task.
n = int(input("Enter your number: "))
x = len(str(n))
i = 0
s = 0
sum = 0
b = ""
while i < x:
    sum += n % 10
    s = n % 10
    n //= 10
    i +=1
    b += f"{s}+"

b_1 = b[0:-1]
print(f"{b_1} = {sum}")