#Input a two-digit natural number and output the sum of its digits. You can
#assume that the input will be a two-digit number and need not check that
#programmatically.
number = int(input("Enter your number: "))
sum = int(str(number)[0]) + int(str(number)[-1])
print(sum)
