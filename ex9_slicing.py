# Slicing

#         01234567890123
parrot = "Norwegian Blue"
#         43210987654321

print(parrot[0:6]) #Norweg
print(parrot[3:5]) #we
print(parrot[0:9]) #Norwegian
print(parrot[:9])  #Norwegian
print(parrot[10:14]) #Blue
print(parrot[10:]) #Blue

print ("#######")

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])
print(parrot)

### Splicing with negative ###

print("#######")
print(parrot[-14:-8])
print(parrot[-4:-2])
print(parrot[-4:12])

### Using a Step in Slice ###
print("########")
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,123;456:789 012;087"
separators = number[1::4]
print(separators)

# For char in number, join char if char not in separators then split it in to a list
values = "".join(char if char not in separators else " " for char in number).split()

# Tip - Using "".join function
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = ":".join(myTuple)
print(x)


#Values was stored as strings
print(type(values[0]))
# Convert strings into int
values_int = [int(val) for val in values]
print(type(values_int[0]))
print(values_int)

### Slicing Backwards ###

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

backwards1 = letters[::-1]
print(backwards1)

###  Exercises ###
# Print only 'qpo' characters
# Print only 'edcba' characters
# Print last 8 characters

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print()
# Funnier mode
print("".join(char if char in "qpo" else "" for char in letters)[::-1])
