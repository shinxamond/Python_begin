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

import random

game = [rock, paper, scissors]

user = int(
  input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)
computer_choice = game[computer]

#0<1<2, 2<0

if user > 2 or user < 0:
  print("You typed an invalid number.")

else:
  user_choice = game[user]
  print(user_choice)
  print("Computer_chose: \n" + computer_choice)
  if computer == 0 and user == 2:
    print("You lose")
  elif user == 0 and computer == 2:
    print("You win")
  elif user < computer:
    print("You lose")
  elif computer < user:
    print("You win")
  elif computer == user:
    print("It's a draw")