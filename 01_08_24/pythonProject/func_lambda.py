# map
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Using map with a lambda function
result = list(map(lambda x: x // 10, numbers))

print(result)



#sorted
#sort this list [["danny", 12] ["bob", 30], ["aaron", 42]]
#sort first by name and then by age.

print(sorted([["danny", 12], ["bob", 30], ["aaron", 42]], key=lambda x: (x[1])))
print(sorted([["danny", 12], ["bob", 30], ["aaron", 42]], key=lambda x: (x[0])))


