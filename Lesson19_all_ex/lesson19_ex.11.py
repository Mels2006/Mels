# 11. Function Exercise:
# Write a function that checks if a given string is a valid email address.
def email(str_1):
    str_1 = str_1.replace('.','@')
    str_2 = str_1.split('@')
    if len(str_2) == 3:
        return True
    return False
    
print(email('a-z@.a-z'))
