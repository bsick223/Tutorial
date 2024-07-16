# str.format() =    optional method that gives users
#                   more control when displaying output

name = 'Brendan Sick'
time = "time"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:23}. Nice to meet you".format(name))
print("Hello, my name is {:<23}. Nice to meet you".format(name)) # left aligned
print("Hello, my name is {:>23}. Nice to meet you".format(name)) # right aligned
print("Hello, my name is {:^23}. Nice to meet you".format(name)) # center aligned








#print(f"Hello, my name is {name:<22}. Nice to meet you")








#print(f"Hello this is my first {time}")

text = f"Hello this is my first {time}"
#print(text)




#print("Hello, this is my first format {day}".format(day = "today"))