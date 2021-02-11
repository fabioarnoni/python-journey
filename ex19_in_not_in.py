# In and Not in

# IN
parrot = "Norwegian Blue"
letter = input("Enter a character or a word: ")
if letter in parrot:
    print("{} is in {}.".format(letter, parrot))
else:
    print("{} is NOT in {}.".format(letter, parrot))

# Not in
activity = input("What would you like to do today: ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")