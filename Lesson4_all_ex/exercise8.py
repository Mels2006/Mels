#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.
num1 = int (input("Input three integers: "))
num2 = int (input("Input three integers: "))
num3 = int (input("Input three integers: "))
if num1 <= num2 <= num3 or num1 >= num2 >= num3:
    print("Sorted")
else:
    print("Unsorted")