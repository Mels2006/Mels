#Arrange string characters such that lowercase letters should come first
words = ["PyNaTive"]
lower = ""
upper = ""

for word in words:
    for char in word:
        if char.islower():
            lower += char
        else:
            upper += char

arranged_string = lower + upper
print(arranged_string)
