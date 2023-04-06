from replit import clear
import random
from hangman_words import word_list  #모듈 임포트 첫 번째 방법(사용시 이름)
import hangman_art  #모듈 임포트 두 번째 방법(사용시 모듈.이름)
#from hangman_art import logo, stages #모듈 임포트 세 번째 방법(사용시 이름. 한 번에 여러 개 임포트)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in display:
        print(f"You've already guess '{guess}'.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])