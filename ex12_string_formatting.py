# String Formatting

# Strings  without alignment
for i in range (1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

# Strings formatted
for i in range (1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# Strings can be aligned to left, right or centrally
for i in range (1, 13):
    print("No. {0:<2} squared is {1:>3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Formatting strings using decimal configuration
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print()

# If you don't provide field values, the function will use the available values sequentially
for i in range (1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))