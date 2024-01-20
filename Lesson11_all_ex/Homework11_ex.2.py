# Write a Python function to calculate count of each letter in string
def count_letters(input_string):
    letter_count = {}
    for letter in input_string:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

input_string = "abracadabra"
result = count_letters(input_string)


print(result)


 


