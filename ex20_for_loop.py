# For Loops

#parrot = "Norwegian Blue"

#for character in parrot:
#    print(character)


print()

number = "9,123;456:789 012;087"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

# For char in number, join char if char not in separators then split it in to a list
values = "".join(char if char not in separators else " " for char in number).split()

print(values)

## Exercise ##

# Print only Upper case letters

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for i in quote:
    if i.isupper():
        print(i, end=" ")
        
print()

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char, end=" ")