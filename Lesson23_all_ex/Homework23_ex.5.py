# Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.
words = ["BMW","Mercedes","Audi"]
words_1 = {word:len(word) for word in words if len(word)>3}
print(words_1)