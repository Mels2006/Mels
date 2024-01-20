#Count how many uppercase and lowercase characters are in this sentence.(“The Quick
#Brown Fox”)
sentence = "The Quick Brown Fox"

uppercase_count = 0
lowercase_count = 0

for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print(f"Uppercase characters: {uppercase_count}")
print(f"Lowercase characters: {lowercase_count}")