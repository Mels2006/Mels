# Print Prime Numbers Function
# Write a function that prints all prime numbers up to a given limit.
def is_prime(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    if num > 1 and is_prime(num):
        print(num)
