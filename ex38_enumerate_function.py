# Using the enumerate function

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
chosen_parts = []
current_choice = ""

while current_choice != 0:
    print("Please select the computer part you want to add: \n")
    for number, part in enumerate(computer_parts):
        print("{0}: {1}".format(number + 1, part))
    if current_choice in (i for i in range(computer_parts)):
        print(current_choice)
    current_choice = int(input())