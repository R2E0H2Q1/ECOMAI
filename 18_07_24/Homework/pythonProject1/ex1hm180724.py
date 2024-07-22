# 1. Basics lists:
# a. Create an empty list and insert the numbers 80-99 into it in the for loop using .append().

empty_list: list[input] = [] #empty list

for numbers in range(80, 100): #Iterate numbers from 80 to 99.
    empty_list.append(numbers) #With .append(), you can add items to the end of an existing list object.
    print(f"{numbers}", end=" ")

print()

# b. Print the first element in the list you created (hint index 0)

print(f"The first element on the list is: {empty_list[0]}")

# c. Print the last element in the list you created (hint index-1)
print(f"The last element on the list is: {empty_list[-1]}")

# d. Print how many elements are in the list

print(f"There are {len(empty_list)} elements on the list!")

# e. Print the terms in index 3 to 12 inclusive (hint use colons)

print(f"The numbers included between index 3 and including 12 are: {empty_list[3:13]}")

# f. Print the members from index 3 to the end of the list (hint use semi-empty colons)

print(f"The numbers from index 3 to the end of the list are:  {empty_list[3: ]}")

# g. Print the members from the beginning of the list to index 9 (hint use colons)

print(f"The numbers from index 0 to index 9 are:  {empty_list[0: 9]}")

# h. Insert the number 999 in the center of the list (hint insert)

empty_list.insert(10, 200)
print(f"To new list including value 200 after index 10 is: {empty_list}")

# i. Print the list in reverse order (cue double colons with -1)

print(f"The list in reverse order is as follows: {empty_list [::-1]}")

# j. Print the list elements only at the odd indexes (hint once with a colon and then the skip)

print(f"The odd numbers on the list are: {empty_list[1 :: 2]}")