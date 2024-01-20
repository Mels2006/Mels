#  Write a program that calculates the sum of
# numbers from 1 to a user-defined limit using a
# while loop.
i = 1
result = 1
number = int(input("Enter your number: "))
while i < number:
     i+=1
     result+=i
print(result)