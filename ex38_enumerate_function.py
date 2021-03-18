# Using the enumerate function

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
chosen_parts = []
current_choice = ""

while current_choice != -1:
    print("Please select the computer part you want to add: \n")
    for number, part in enumerate(computer_parts):
        print("{0}: {1}".format(number +1, part))
    if current_choice in (prt_num for prt_num, prt_name in enumerate(chosen_parts)):
        print("Removing {}\n".format(current_choice))
        chosen_parts.remove(computer_parts[current_choice])
        print("Your current list: {}".format(chosen_parts))
    elif current_choice in (prt_num for prt_num, prt_name in enumerate(computer_parts)):
        print("Adding {}\n".format(current_choice))
        chosen_parts.append(computer_parts[current_choice])
        print("Your current list: {}".format(chosen_parts))
    else:
        print("Please inform a valid number: \n")
    current_choice = int(input()) - 1


print(chosen_parts)