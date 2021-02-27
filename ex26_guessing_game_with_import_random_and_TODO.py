# The guessing game with import, random and TO-DO
import random

highest = 10
answer = random.randint(1, 10)
print(answer) #TODO: Remove it after testing
user_input = ""
guess = 0

print("Please guess a number between 1 and {}: ".format(highest))


while guess != answer:
    user_input = input()
    if user_input not in "012345678910":
        print("You did not entered a valid number. Please try again")
        continue
    else:
        guess = int(user_input)

    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print("Guess is higher")
        else:
            print("Guess is lower")
