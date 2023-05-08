#import random
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def check_answer(number, answer, attempts):
  """checks answer against guess number. Returns the number of attempts remaining."""
  if number == answer:
    print(f"You got it! The answer was {answer}")
  elif number < answer:
    print("Too low.")
    return attempts - 1
  elif number > answer:
    print("Too high.")
    return attempts - 1


def guess():
  print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
  )
  answer = randint(1, 100)

  attempts = set_difficulty()

  number = 0
  while number != answer:
    print(f"You have {attempts} attempts remaining to guess the number.")
    number = int(input("Make a guess: "))

    attempts = check_answer(number, answer, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
    elif number != answer:
      print("Guess again.")


#=====game start=====##

guess()
