# Mutable objects

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

print()

shopping_list += ["coockies"]

print(id(shopping_list))
print(id(another_list))

print()

a = b = c = d = e = f = another_list
print(a)

print()
print("adding cream")
b.append("cream")
print(c)
print(d)
print(shopping_list)

