# While Loops
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1


print("#" *80)

j = 0
End = True
while End == True:
    print("j is now {}".format(j))
    if j == 10:
        End = False
    j += 1

print("#" *80)

available_exits = ['north', 'south', 'east', 'west']
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a Direction: ")

print("aren't you glad you got out of there?")