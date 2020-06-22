# Checks if your entered password is valid
# example for valid password: Tr$macs187


import time as t

password_charakters = []
password_charakters_which_are_digits = []
password_charakters_which_are_special = []
password = input("Passwort: ")

print(" ")
print(" ")

if len(password) >= 5 and len(password) <= 10:
    if password.count(" ") == 0:
        password_charakters = " ".join(password).split(" ")
        for character in password_charakters:
            if character.isdigit():
                password_charakters_which_are_digits.append(character)
        if len(password_charakters_which_are_digits) >= 1:
            if password.isalnum():
                print("Invalid password")
            else:
                print("Valid password")
                print(" ")
                print(" ")
                t.sleep(5)
        else:
            print("Invalid password")
    else:
        print("Invalid password")
else:
    print("Invalid password")