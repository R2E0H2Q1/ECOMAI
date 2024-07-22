# List are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
# all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# index:               0  1   2  3  len=4 #Index is the position that a values occupies on a list. Starting always with 0.
numbers: list[int] = [10, 2, -1, 4]
#                    200 201 202 203
#     numbers==#200
#       numbers[1]
print(numbers) # Print the list called "numbers".
print(f"numbers[0] = {numbers[0]}") # 10
print(f"numbers[3] = {numbers[3]}") # 10
#print(numbers[4]) # Error - Because there isn't an object in position 4.
print(f"list length = {len(numbers)}") #The len() function is use to determine how many items a list has.

# for. use it when we need the index
for i in range(0, len(numbers)):
    number = numbers[i] #number is equal to the store value in the provided index.
    print(f"numbers[{i}] = {numbers[i]}", end=" | ")  # 10
print()

# [10, 2, -1, 4]
# for-each
for number in numbers:
    print(number, end=" ")
print()

for c in "Hello": #This line initiates a for loop that iterates over each character (c) in the string "Hello", one by one.
    print(c, end= " ")
print()

# The loop iterates through each character in "Hello": 'H', 'e', 'l', 'l', 'o'.
# Each character is printed with print(c, end=" "). Because of end=" ", each character is printed with a space after it instead of a newline.
# After the loop completes, print() without any arguments is called, which prints a newline character, moving the cursor to the next line.
# The print(c, end=" ") statement does not print 'H e l l o' as a single string. Instead,
# it prints each character of "Hello" separated by spaces, and then print() moves the output to the next line.

# index
#   0  1   2  3
# [10, 2, -1, 4]
print(f"numbers[0: 3] = {numbers[0: 3]}") # [10, 2, -1] # Print from the list "numbers" a list using index 0 up to index 3(indexs0,1,2)/ Respuesta: numbers[0: 3] = [10, 2, -1]
print(f"numbers[:3] = {numbers[:3]}")   # [10, 2, -1] # Print from the list "numbers" a list from initial indx up to indx 3(indexs0,1,2)/ Respuesta: numbers[:3] = [10, 2, -1]
print(f"numbers[:] = {numbers[:]}")   # [10, 2, -1, 4] # Print everything on the list. / Respuesta: numbers[:] = [10, 2, -1, 4]
print(f"numbers[2: 4] = {numbers[2: 4]}")   # [ -1, 4] #Print between index 2 and the end. / Respuesta: numbers[2: 4] = [-1, 4]
print(f"numbers[2:] = {numbers[2:]}")   # [ -1, 4]
print(f"numbers[0:4:2] = {numbers[0:4:2]}")   # [10, -1]
print(f"numbers[::-1] = {numbers[::-1]}")   # [4, -1, 2, 10] # Prints the list in reverse order
print(f"numbers[len(numbers) - 1] = {numbers[len(numbers) - 1]}")   # [4]
print(f"numbers[-1] = {numbers[-1]}")   # [4]
print(f"numbers[-2] = {numbers[-2]}")   # [-1]

print()
print('original', numbers) # Prints the original content of the list: numbers.
numbers[0] = 200 #assigns a new value of 200 for index 0 on the list called "numbers".
print('after numbers[0] = 200', numbers) #prints the list numbers with the new added value for index 0.
numbers.insert(2, 444) #using .insert after the list name you can change the value of an index using a coordenate of (index, new value).
print('after numbers.insert(2, 444)', numbers)#prints the list numbers with the new inserted value for index 0.
print()

# Lists and loops
# input grades from user until entered -999
# ignore < 0 or > 100
# store all of the grades
grades: list[int] = []
while True:
    grade: int = int(input("enter grade [-999 to exit]:"))
    if grade == -999:
        break
    if grade < 0 or grade > 100:
        continue
    grades.append(grade) # insert at the end of list "grades" the content of "grade"

print(grades)
print(f"max(grades) = {max(grades)}") #using {max(list_name)} we print the maximum value inserted in the list "grades"
print(f"min(grades) = {min(grades)}")
print(f"sum(grades) = {sum(grades)}")
print(f"len(grades) = {len(grades)}")
print(f"avg(grades) = {sum(grades) / len(grades) : .2f}")

import statistics
print(f"statistics.mean(grades) = {statistics.mean(grades) : .2f}") #The statistics.mean() method calculates the average of the given data set/
                                                                    # adding up all the given values, then divide by how many values there are.
