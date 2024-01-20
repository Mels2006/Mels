# Write a function in python to read the content from a text file "example.txt" line by line
# and display the same on screen.
import os

def display_lines(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                print(line)
file_path = 'example.txt'
display_lines(file_path)