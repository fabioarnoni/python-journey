# Printing information in splitted lines

splitString = "This string \n has been split over\n several lines"

print(splitString)

tabbedString = "1\t2\t3\t4\t5\t6"

print(tabbedString)

print('The pet shop owner said "No, no \'e\'s uh, ... He \'s resting".')
print("The pet shop owner said \"No, no 'e's uh, ... He 's resting\".")
print("""The pet shop owner said "No, no 'e's uh, ... He 's resting". """)

anotherSplitString = """This string
has been split over
several lines"""

print(anotherSplitString)


notSplittedString = """This string has NOT been \
splited over \
several lines"""

print(notSplittedString)

# Scaping Back slashes
print("C:\\Users\\timbuchalka\\notes")
print(r"C:\Users\timbuchalka\notes")