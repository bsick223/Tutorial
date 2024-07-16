# logical operators (and, or, not)
# use to check if two or more conditional statements are true

temp = int(input("What's the temperature outside?: "))

# if temp >= 0 and temp <= 30:
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outside!")

