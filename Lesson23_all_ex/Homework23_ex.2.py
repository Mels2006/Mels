# Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string
string = "abracadabra"
frequency = {char: string.count(char) for char in string}

print(frequency)
