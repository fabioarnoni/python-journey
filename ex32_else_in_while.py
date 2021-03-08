# Else in While - Another example

# Continue and break in while loops + Else in While

available_exits = ['north', 'south', 'east', 'west']
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a Direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there?")