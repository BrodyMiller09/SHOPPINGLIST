# cs-grocceriescode
# This is my code for Computer Science 30 shopping list
# Lists assignment
# Grocery list

# Starting code
groceries = ["milk", "butter", "eggs", "bacon", "hashbrowns"]

# Nested list
prices = [
    ["milk", 4],
    ["butter", 6],
    ["eggs", 12],
    ["bacon", 24],
    ["hashbrowns", 13]
]

# Code
shopping_list = []

print("Welcome to shopping list!")

# Available groceries
print("\nAvailable groceries:")
print(groceries)

# Adding items
item = input("What groceries are you wanting to add to your list? ")
shopping_list.append(item)

# Add another item
item = input("What else would you like to add? ")
shopping_list.append(item)

# Print list
print("\nYour shopping list:", shopping_list)

# Length
print("Number of items:", len(shopping_list))

# Slice
print("First 3 available groceries:", groceries[:3])

# Remove items
remove = input("Which item would you like to remove? ")

if remove in shopping_list:
    shopping_list.remove(remove)

print("Final shopping list:", shopping_list)