# Write a Python program that prompts the user to enter a positive integer and then prints
# all the numbers from 1 to that number using a while loop.
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    i = 1
    while i <= n:
        print(i)
        i += 1

