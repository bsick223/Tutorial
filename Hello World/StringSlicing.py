# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
#           [inclusive:exclusive]
name = "Brendan Sick"

first_name = name[:7]
last_name = name[8:]
funky_name = name[0:13:4]
funky_name2 = name[::4]
reversed_name = name[::-1]

print(reversed_name)

print(first_name)
print(last_name)
print(funky_name)
print(funky_name2)


