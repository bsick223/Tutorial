# Loop Control Statements = change a loops execution from its normal sequence


# break =       used to terminate the loop entirely
while True:
    name = str(input("Enter your name: "))
    if name != "":
        break


# continue =    skips to the next iteration of the loop
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


# pass =        does nothing, acts as a placeholder
for i in range(1, 21):

    if i == 13:
        pass
    else:
        print(i)



