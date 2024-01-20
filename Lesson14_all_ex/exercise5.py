# Write a python program to read a file, a.txt line by line.
import os

file_path = 'a.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)