# 4 Use of map. source string:
# Create a list of words that will contain the following fruits: "Mango", "Orange", "Banana", "Apple", " ", "Strawberry", "Pineapple", "Grapes", "Watermelon"

fruit_lst = ["Mango", "Orange", "Banana", "Apple", " ", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(f"The original list is: {fruit_lst}")

# Use map and lambda to get a new list that will contain:
# a. Each fruit is in reverse alphabetical order. hint [-1 ::]

print("The list in reverse order is as follow: ", list(map(lambda x: x[:: -1], fruit_lst)))

# b. First letter of each fruit

print(f"The first letters of the items list are:", list(map(lambda x: x[0], fruit_lst)) )

# c. The fruit is all in capital letters

print(f"List in uppercase: ", list(map(lambda x: x.upper(), fruit_lst)))

# d. length of each fruit. For example, Apple will become the number 5. (the new list will contain only numbers)

print(f"The length of the items on the list are: ", list(map(lambda x: len(x), fruit_lst)))