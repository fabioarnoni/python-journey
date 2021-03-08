# Else in While (Using the Hilo game as example)
low = 1
high = 1000
guesses = 0
guess = 0

print("Please think of a number between {} and {}: \n".format(low, high))
input("Press Enter: ")

while high != low:
    print("Guessing a number between {} and {}".format(low, high))
    guess = low + (high - low) // 2
    hi_low = input("My guess is {}. Should I Guess higher or Lower? "
                   "Please enter l for low, h for high or c for correct: "
                   .format(guess)).casefold()
    if hi_low == "h":
        low = guess + 1
    elif hi_low == "l":
        high = guess - 1
    elif hi_low == "c":
        print("I guessed it in {} guesses".format(guesses))
        break
    else:
        print("Please enter l, h or c")
    guesses += 1
else:
    print("you thought of a number {}".format(low))
    print("I got it in {} guesses".format(guesses))
