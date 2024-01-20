#Write a Python script that takes a list of words and return the longest word and the
#length of the longest one.
words = ["word", "is", "apple"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(f'{longest} {len(longest)}')