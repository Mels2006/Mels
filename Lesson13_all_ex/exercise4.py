# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
# 2 filter
nums = [2,5,8,9,7,6,3]
evens = list(filter(lambda x: x % 2 == 0,nums))
print(evens)
odds = list(filter(lambda x:x % 2 == 1,nums))
print(odds)