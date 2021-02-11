# Booleans - True or False
day = "Saturday"
temperature = 25
raining = False

if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")


if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

print ()

if 0:
    print("True")
else:
    print("False")

name = input("Please enter yout name: ")
if name:
    print("Hello {}.".format(name))
else:
    print("Are you a man with no name?")
