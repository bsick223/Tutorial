# while loop = a statement that will execute a block of code
# as long as true

#name = ""

#while len(name) == 0:
    #name = input("Enter your name: ")

#print("Hello " +name)

name = None

while not name:
    name = input("Enter your name: ")

    print("Hello "+name)