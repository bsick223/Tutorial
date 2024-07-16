# nested loop =     The "inner loop" will finish all of its iterations
#                   before finishing one iteration of the "outer loop"

# outer loop
rows = int(input("How many rows? "))

# inner loop
columns = int(input("How many columns? "))


symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #prevents new line
    print()
levels = 5

# rows
for i in range(levels):

    # columns
    for j in range(levels - i -1):
        print(" ", end="")
    for k in range(2*i + 1):
        print("*", end="")
    print()















