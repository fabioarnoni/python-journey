# Immutable objects

result = True
another_result = result
print(id(result))
print(id(another_result))

print()

result = False
print(id(result))

print()

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

print()

result += "ish"
print(id(result))
print(id(another_result))