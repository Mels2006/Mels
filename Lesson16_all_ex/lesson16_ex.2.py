# Write a python program to catch error a num dividing by zero
def catch_error(a,b): 
    try:
        x = a/b
        print(x)
    except ZeroDivisionError as e:
        print("You can not divide on 0")
print(catch_error(10,0))