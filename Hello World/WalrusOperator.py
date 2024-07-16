# walrus operator :=

# assigns values to variables as part of larger expression

# happy = True
# print(happy)

print(happy := True)
"""
foods = list()
while True:
    food = input("what food do you like: ")
    if food == "quit":
        break
    foods.append(food)
"""

foods = list()
while food := input("what food do you like?: ") != "quit":
    foods.append(food)
