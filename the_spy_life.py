input = input("Encoded Message > ")
output = ""

splitted_input = (".".join(input)).split(".")

for char in splitted_input:
    if char.isalpha() or char == " ":
        output = char + output
    else:
        continue

print(output)