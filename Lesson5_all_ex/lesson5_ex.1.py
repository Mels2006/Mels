# check how many ‘a’ characters are in inputed string.
user_input = input("Enter some text: ")

count_of_a = 0

for char in user_input:
    if char.lower() == 'a':
        count_of_a += 1

print("Number of 'a' characters:", count_of_a)

