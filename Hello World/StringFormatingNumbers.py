# str.format() =    optional method that gives users
#                   more control when displaying output

#number = 3.14159
#print("The number pi is {:.2f}".format(number))

number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number)) # octal
print("The number pi is {:X}".format(number)) # hexidecimal number
print("The number pi is {:e}".format(number)) # Scientific notation