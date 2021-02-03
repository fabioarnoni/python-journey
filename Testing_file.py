letters = "abcdefghijklmnopqrstuvwxyz"


print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print()
# Funnier mode
print("".join(char if char in "qpo" else "" for char in letters)[::-1])