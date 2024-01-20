#  Prime number checker
#  Develop a program that checks if a given number is prime using a while loop. Ask
#  the user for input and print whether the number is prime or not.
i = 2
n = int(input("Enter your number: "))
res = True
while i < n/2:
    if n % i == 0:
        res = False
        break
    i += 1
print(res)
