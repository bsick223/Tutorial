# function = block of code which is executed only when it is called

# paramaters recieve
#def hello(first_name, last_name, age):
    # pass // do this to pass
    #print("Hello " +first_name +" "+ last_name)
    #print("You are "+str(age)+" years old.")
    #print("Have a nice day! ")
# hello("Brendan Sick") #arguments are information you are sending

#hello("Brendan", "Sick", 25)





# make a quiz game using functions
# validate the question with function
# or use the whole thing as a function.


print("Welcome to my quiz!")
score = 0

def quiz_question(question, answer):
    user_answer = input(question)

    try:
        user_answer = int(user_answer)
    except ValueError:
        user_answer = user_answer.strip().lower()

    if user_answer == answer:
        print("you got it!")
        global score
        score += 1
    else:
        print("wrong one!")

    print("Score is "+str(score))



quiz_question("How many days in a week?: ", 7)

quiz_question("How many states in USA?: ", 50)

quiz_question("What is the opposite of day? ", "night")

print("Final score is " + str(score) + "/3")


