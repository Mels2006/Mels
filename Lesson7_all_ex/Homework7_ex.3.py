#Write a Python program that input a sentence and return the longest word and the length
#of the longest one.
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f'The longest word is "{longest_word}" and its length is {len(longest_word)}.')