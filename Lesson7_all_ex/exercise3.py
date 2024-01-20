#Write a program to check if two strings are balanced. For example, strings s1 and
#s2 are balanced if all the characters in the s1 are present in s2. The character’s
#position doesn’t matter.
def are_strings_balanced(s1, s2):
    for char in s1:
        if char not in s2:
            return False

    return True


s1 = "Yf"
s2 = "PYnative"
result = are_strings_balanced(s1, s2)
print(result)
