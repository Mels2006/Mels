# Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters.
import os
file_path = "example.txt"
def display_words(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
             text = file.read()
             words = text.split()
        short_words = [word for word in words if len(word) < 4]

        print(short_words)
        
display_words(file_path)

    