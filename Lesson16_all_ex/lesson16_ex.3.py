# Write a python program that will raise an exception (Invalid
# File) if text file contents first symbol is starting with number
def raise_an_exception(filename):
    f = open(filename,"r")
    x = f.read()
    if x[0].isdigit:
        raise Exception("InvalidFile")
print(raise_an_exception("a.txt"))
