# item = "bag"
# print(item)
#     Create an empty list called items.
#     Prompt the user to enter four items using input() and add them to the list.
#     Display the list after all items are entered.
#     Allow the user to update an item in the list:
#         Ask the user for a position (1-4) to update.
#         Replace the selected item with a new value provided by the user.
#     Display the updated list.
#     Allow the user to remove an item from the list:
#         Ask the user for a position (1-4) to remove.30
#         Remove the selected item from the list.
#     Display the final list after removal.

items = []

items.append(input("Enter first item: "))
items.append(input("Enter second item: "))
items.append(input("Enter third item: "))
items.append(input("Enter fouth item: "))

print(items)

# update item
update_next_item = int(input("\n Enter the item number(1-4) to update: " )) - 1
new_item = input("Enter the new item: ")


item_to_pop = input("\nEnter item to pop")
item_to_pop = items.pop(3)
print(item_to_pop)

print(update_next_item, items)


