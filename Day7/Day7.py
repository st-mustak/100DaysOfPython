# TODO-1: make a word list
# TODO-2:
# TODO-3:
# TODO-4:
# TODO-5:


import random

from arts import hangman
from arts import thumbs_up

print("\n------***  Welcome to the HANGMAN-WORD Game  ***-------\n\n")
word_list = ['meditation', 'oxygenation', 'visualization',
             'exercise', 'reading', 'scribing', 'learning',
             'solution']
word = random.choice(word_list)



word_space = ""

for letter in word:
    word_space += "_"
print(f"Let's Guess the word: {word_space}")

c = 1
game_end = False
correct_letters = []
lives = 8
while not game_end:
    display = ""
    user_letter = input("\nEnter a letter : ").lower()
    for letter in word:
        if letter == user_letter:
            display += user_letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if display == word:
        game_end = True
        print(f"\nWow! You have made it. Thumbs Up. {thumbs_up} ")

    if user_letter not in word:
        lives -= 1
        print(f"Oops! Wrong Entry . Your Lives left {lives} out of 8. {hangman[7-lives]}")

    elif game_end is not True:
        print("Great! You have entered correct letter. Keep on Guessing. ")

    if lives == 0:
        print("\nSorry, You Hanged! you have no life left. ")
        game_end = True
