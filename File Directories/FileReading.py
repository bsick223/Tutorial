try:
# automatically closes the file
    with open('text.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("That file was not found.")



# returns true if closed
# print(file.closed)