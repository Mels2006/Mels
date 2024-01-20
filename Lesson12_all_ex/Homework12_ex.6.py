# Count Words Function
# Write a function that counts the number of words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

my_sentence = "Manchester City is the best club in the world."
word_count = count_words(my_sentence)
print(word_count)