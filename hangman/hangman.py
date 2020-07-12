# Made to play an normal round of hangman


import time as t
import os
import random

misses = 0
gamemode_picked = False
guesses = ""
word = ""
words = open(r"\python-challenges\hangman\words.txt").read().split()

# Choose your gamemode

print("Choose your gamemode: \n 'solo' (you guess the word the game challenges you to) \n 'multi' (one player types in a word, the other has to guess it)\n")
gamemode = input("> ")

while gamemode_picked == False:
    if(gamemode == "solo"):
        searched_word = random.choice(words)
        gamemode_picked = True
    elif(gamemode == "multi"):
        os.system('cls')
        searched_word = input("The word to search for goes here > ")
        gamemode_picked = True
    else:
        print("The given input is not a valid gamemode!")
        gamemode = input("> ")

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
            print("\n\nGAME OVER\nThe word was: " + searched_word + "\n\n")
            t.sleep(2)
            break
        continue
