# For Ranges

for i in range(1, 20):
    print(i, end=" ")

print()

for i in range(20):
    print(i, end=" ")

print()

for i in range(0, 10, 2):
    print(i, end=" ")

print()

for i in range(0, 10, 2):
    print(i, end=" ")

print()

for i in range(10, 0, -2):
    print(i, end=" ")

print()

age = int(input("How old are you? "))

if age in range(16, 66):
    print("have a good day at work")
else:
    print("Enjoy your free time")

# Exercise using for loops
# Write a program to print out all numbers from 0 to 100 that are divisible by 7

# This solution uses a if statement with rest division
for i in range(100):
    if i % 7 == 0:
        print(i)

# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)

# This solution uses a slice
for i in range(101)[::7]:
    print(i)