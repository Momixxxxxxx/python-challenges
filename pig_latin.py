# Takes an Englisch phrase
# and moves the first char of each word to the end of that word and expands the word by "ay"
# example: "My mother is old" -> "yMay othermay siay ldoay"


english_words = list(input("Input: ").split(" "))
se = []

for i in range(len(english_words)):
    se.append(english_words[i][1:] + english_words[i][0] + "ay")
s = ""

for i in range(len(english_words)):
    s = s + se[i] + " "
print(s)
