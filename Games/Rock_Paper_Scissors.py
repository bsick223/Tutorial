import random

choices = ["rock", "paper", "scissors"]

while True:

    try:
        player_choice = input("Rock, Paper, or Scissors? ").strip().lower()
        if player_choice in choices:
            break
    except:
        print("please enter a rock, paper, or scissors.")
        continue

computer_pick = random.choice(choices)

if player_choice == computer_pick:
    print("Tie")

elif player_choice == 'rock' and computer_pick == 'scissors':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You win")
elif player_choice == 'paper' and computer_pick == 'rock':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You win")
elif player_choice == 'scissors' and computer_pick == 'paper':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You win")
elif player_choice == 'rock' and computer_pick == 'paper':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You lose")
elif player_choice == 'paper' and computer_pick == 'scissors':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You lose")
elif player_choice == 'scissors' and computer_pick == 'rock':
    print(f"Player picked {player_choice}")
    print(f"Computer picked {computer_pick}")
    print("You lose")







