
# Python Challenges

### Hangman

It's made to play a casual round of hangman.

First, you can choose, if you wanna play alone or with a friend.

If you play with a friend, one of you types in a word to search for, the other one can guess.

If you play alone, the program will challenge you with a word, random picked from a 200+ word list.

*you have 6 misses, like normal hangman*

**Important:** when you clone or download the whole repository, everything will work fine, but if you want only the hangman game, don't forget to download the word list and maybe you have to adjust the path of the list in the *hangman.py* in line 12:

```python
words = open("YOUR words.txt PATH").read().split()
```

You could also make your own wordlist, simply make a *your_filename*.txt document and write down your words, each one in a single line, without commas in between.
And don't forget to link it into the *hangman.py* file, like explained above.

---

### Remove Spaces

A simple programm, which removes the spaces from your input

---

### Password Validator

Enter a password and the programm will check for you, if it's a valid one

Example: *Tr$macs187* is **valid**, *icecreamcone* is **not**

---

### Pig Latin

It takes an Englisch phrase
and moves the first char of each word to the end of that word and expands the word by "ay"

Example: *"My mother is old"* -> *"yMay othermay siay ldoay"*

---

### Youtube Link Finder

Takes a youtube link as an input and outputs only the video ID

Example: *https://youtube.com/watch?v=kbxkq_w51PM* -> *kbxkq_w51PM*

---

### The Spy Life

The programm takes a encoded phrase, removes all nonalphabetic characters and turns the whole phrase around.

Example: *d89%l++5r19o7W 9o=l6945le9H* -> *Hello World*
