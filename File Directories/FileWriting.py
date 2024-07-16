
text = "Have a nice day! see yea"


# typically the 2nd argument is 'r' for read
# you can do 'w' for write.  This overwrites
# 'a' will append

with open('text.txt', 'a') as file:
    file.write(text)