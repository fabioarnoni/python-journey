# Operator precedence
a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) # Result given as float
print(a // b) # Result given as integer
print(a % b) # Division Rest

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print(a / (b * a) / b)