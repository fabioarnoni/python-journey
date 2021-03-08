# Printing information in splitted lines

split_string = "This string \n has been split over\n several lines"

print(split_string)

tabbed_string = "1\t2\t3\t4\t5\t6"

print(tabbed_string)

print('The pet shop owner said "No, no \'e\'s uh, ... He \'s resting".')
print("The pet shop owner said \"No, no 'e's uh, ... He 's resting\".")
print("""The pet shop owner said "No, no 'e's uh, ... He 's resting". """)

another_split_string = """This string
has been split over
several lines"""

print(another_split_string)


not_split_string = """This string has NOT been \
splited over \
several lines"""

print(not_split_string)

# Scaping Back slashes
print("C:\\Users\\timbuchalka\\notes")
print(r"C:\Users\timbuchalka\notes")