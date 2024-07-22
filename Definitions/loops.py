#For Loops
#A for loop is used for iterating over a sequence, that is either a list, a tuple, a dictionary, a set, or a string.
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits: #in is check to check if a value exists within a sequence.
  print(x, end=(" "))

####################################################################################################################################################################
#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x,)
  if x == "banana":
    break #when gets to banana the loop exits because of the break statement
    print(x, end=(" "))

  ####################################################################################################################################################################
  #With the continue statement we can stop the current iteration of the loop, and continue with the next:
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    if x == "banana":
      continue
    print(x, end=(" "))

####################################################################################################################################################################
#The range function: To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
# range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

####################################################################################################################################################################
#The first two digits provide the range and the third the number that will be added to the next one.
for x in range(2, 30, 3):
  print(x, end=(" "))

####################################################################################################################################################################
#Else in For Loop. The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Print all numbers from 0 to 5, and print a message when the loop has ended:
#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  print(x)
else:
  print("Finally finished!")

####################################################################################################################################################################
#Nested Loops: A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

####################################################################################################################################################################
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6: #while "i" is smaller than 6
  print(i) #continue to print "i" in the meantime that "i" is least than 6
  i += 1 #add 1 with each printing

####################################################################################################################################################################
#In Python, a while True loop is a construct that creates an infinite loop.
# This means that the loop will continue to execute indefinitely until a break condition is met or the program is terminated externally
#while True:
    # Code block to be executed repeatedly
    # until a break statement is encountered
    # or the program is terminated
    # Typically, some condition will be checked
    # within the loop to determine when to break out
    # of the loop.
    # To break out of the loop you can use the 'break' statement.
    #I am even if
#Start
x: int = 1;
while x < 20: # condition is tested before entering 1st cycle
    print(x, end=" ");
    x = x + 1;
    # --
print('finish\nfinish')
#Stop