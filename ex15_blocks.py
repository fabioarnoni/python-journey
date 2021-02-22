# Python Blocks

# for loop
for i in range(1, 13):
    print("No. {:2} squared is {:2} and cubed is {:4}.".format(i, i **2, i **3))
print("*" * 80)

print()

# if statements

name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))

if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years.".format(18 -age))

# elif

if age < 18:
    print("Please come back in {0} years.".format(18 - age))

elif age ==900:
    print("Sorry, Yoda, you die in return of the Jedi")
else:
    print("You are old enough to vote")