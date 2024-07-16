# -----------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("# -----------------------------")
        print(key)

        # provide all the options
        # after that it goes back to the key
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        # check the answer and return a score
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)



# -----------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    pass


# -----------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")

    print("Answers: ", end="")

    # display all values in dictionary
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print(f"Your score is: {score}%")



# -----------------------------
def play_again():


    response = input("Do you want to play again? (yes/no): ")
    response = response.upper().strip()

    if response == "YES":
        return True
    else:
        return False
# -----------------------------


questions = {
    "Who created Python? ": "A",
    "Who is a great programmer and an amazing person?": "D",
    "What year was Python created? ": "C",
    "Python is attributed to which comedy group?: ": "A"
}

options = [["A. Guido van Rossum", "B. Anthony Burks", "C. Tony Herson", "D. Elon Musk"],
           ["A. Billy Einstein", "B. Tony Robbinson", "C. Joe Cepal", "D. Brendan"],
           ["A. 1882", "B. 2014 ", "C. 1991", "D. 1996"],
           ["A. Monty Python", "B. Lonely Island", "C. SpongeBob SquarePants", "D. Smosh"]]

new_game()

while play_again():
    new_game()

print("See ya later!")





# more options? here's a template
#               ["A. ", "B. ","C. ","D. "]
