# Continue and Break in for loops
shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
found_at = None
item_to_find = 'spam'

for i in shopping_list:
    if i != 'spam':
        print(i)
print("#" * 80)

for i in shopping_list:
    if i == 'spam':
        continue  # Ignore current item and jump to next item
    print(i)

print("#" * 80)

shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
found_at = None
item_to_find = 'spam'

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break  # Jump out of the loop, avoiding it to continue iterating

# Best approach
# if item_to_find in shopping_list:
#    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
