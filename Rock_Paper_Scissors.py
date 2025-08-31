import random

options=("Rock","Paper","Scissors")
running=True

while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice (rock,paper,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("its tie")
    elif player== "Rock" and computer =="Scissors":
        print("yow win")
    elif player == "Paper" and computer=="Rock":
        print("yow win")
    elif player == "Scissors" and computer=="Paper":
        print("yow win")
    else:
        print("you lose")

    if not input("play again?(y/n):").lower()=="y":
        running=False

print("thanks for playing")
    
