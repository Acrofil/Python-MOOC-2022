# Write your solution here

items_number = int(input("How many items: "))

items = []
i = 1

for i  in range(items_number):
    item_input = int(input(f"Item {i + 1}: "))
    items.append(item_input)

print(items)
