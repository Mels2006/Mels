# Write a function in Python to count and display the total number of words in a text file.
import os
file_path = "example.txt"
def count_and_display_words(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            
            content = file.read()

            
            word_count = len(content.split())

            
            print(word_count)
    
count_and_display_words(file_path)