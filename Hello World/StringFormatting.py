# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # Keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))