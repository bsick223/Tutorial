import random

# generate a random number like 1-6 rolling a dice

def roll():
    random_number = random.randint(1, 6)
    random_number2 = random.random()
    return random_number, random_number2

random_number, random_number2 = roll()

print(random_number)
print(random_number2)