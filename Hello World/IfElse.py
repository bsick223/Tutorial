# if statement = a block of code that will execute if true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a centurion")
elif age >= 18:
    print('You are an adult!')
elif age < 0:
    print("You haven't been born yet")
else:
    print('You are a child')

