# Made to play an normal round of hangman
# First, enter a word to search for
# then place your guessed characters
# you have 6 misses


import time as t
import os

searched_word = input("The word to search for goes here > ")
misses = 0
guesses = ""
word = ""

while True:
    os.system('cls')
    word = ""
    t.sleep(0.2)
    for char in searched_word:
        if(char.lower() in guesses.lower()):
            word += (char + " ")
        else:
            word += "_ "
    
    if(word.replace(" ", "") == searched_word):
        os.system('cls')
        print("\n\n" + "YOU WON" + "\n\n")
        t.sleep(2)
        break

    print("\n\n" + word + "\n\n" + "Misses: " + "× " * misses + "○ " * (6 - misses) + "\n\n")

    guessed_character = input("Your guess > ")
    if(searched_word.lower().__contains__(guessed_character.lower())):
        guesses += guessed_character
        continue
    else:
        misses += 1
        if(misses == 6):
            os.system('cls')
            print("\n\nGAME OVER\n\n")
            t.sleep(2)
            break
        continue
