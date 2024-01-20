# 3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.
def sum_of_numbers_divisible_by_seven(number):
    sum_divisible_by_seven = 0

    for number in number:
        if number % 7 == 0:
            sum_divisible_by_seven += number
    return sum_divisible_by_seven


list = [1, 5, 7, 14, 49, 25, 21]

result_sum = sum_of_numbers_divisible_by_seven(list)

    


    