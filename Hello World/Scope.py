# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

"""
Order of operations:

L = Local
E = Enclosing
G = Global
B = Built-in


"""

name = "Bro" # global variable or scope ( available inside and outside functions)

def display_name():
    name = "Code" # local scope or variable (available only inside this function
    print(name)

print(name)
display_name()