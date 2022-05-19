import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [0, 1, 2]
pictures = [rock, paper, scissors]

player1 = int(input("What do you choose? Tye 0 = Rock, 1 = Paper or 2 = Scissors.\n"))
while player1 not in options:
    print("Wrong selection.")
    player1 = int(input("What do you choose? Tye 0 = Rock, 1 = Paper or 2 = Scissors.\n"))
    
for item in options:
    if player1 == item: 
        print(f"Player choose: {pictures[item]}")

computer = random.choice(options) 
#computer = random.randint(0, 2)
for item in options:
    if computer == item:
        print(f"Computer choose: {pictures[item]}")
    
""" if player1 == computer:
    print("It's a draw.")
elif player1 == 0 and computer == 1:
    print("Computer wins.")
elif player1 == 0 and computer == 2:
    print("Player wins.")
elif player1 == 1 and computer == 0:
    print("Player wins.")
elif player1 == 1 and computer == 2:
    print("Computer wins.")
elif player1 == 2 and player1 == 0:
     print("Computer wins.")
elif player1 == 2 and computer == 1:
    print("Player wins.") """

if player1 == computer:
    print("It's a draw.")
elif player1 == 0:
    if computer == 1:
        print("Computer wins.")
    elif computer == 2:
        print("Player wins.")
elif player1 == 1:
    if computer == 0:
        print("Player wins.")
    elif computer == 2:
        print("Computer wins.")
elif player1 == 2:
    if computer == 0:
        print("Computer wins.")
    elif computer == 1:
        print("Player wins.")


""" 
#Solución profe:
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose...."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choses: ")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw") """
