# 14. Strings Exercise:
# Write a function that capitalizes the first letter of each word in a sentence
def capitalize_words(sentence):
    return sentence.title()


input_sentence = "this is a sample sentence"
result = capitalize_words(input_sentence)

print(f"Capitalized sentence: {result}")
