# The programm takes a encoded phrase, removes all nonalphabetic characters and turns the whole phrase around.
# Example: *d89%l++5r19o7W 9o=l6945le9H* -> *Hello World*

input = input("Encoded Message > ")
output = ""

splitted_input = (".".join(input)).split(".")

for char in splitted_input:
    if char.isalpha() or char == " ":
        output = char + output
    else:
        continue

print(output)