#Count all letters, digits, and special symbols from a given string
input_string = "P@#yn26at^&i5ve"

char_count = 0
digit_count = 0
special_count = 0

for char in input_string:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"Letters: {char_count}")
print(f"Digits: {digit_count}")
print(f"Special symbols: {special_count}")
