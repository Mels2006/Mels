# Write a python program to read the whole text of a file and catch the error if files does not exists.
try:
    f = open("py1.txt","r")
    print(f.read)
except FileNotFoundError as e:
    print("File Doesn't exist")
