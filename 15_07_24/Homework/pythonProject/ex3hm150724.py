# 3.Exercises in a nested loop-
# 1) Receive from the user a positive number greater than 0, and print the following symmetrical shape
# For example, if we received 5 print:
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1

number = int(input("Please enter a positive number greater than 0: "))

for i in range(1, number + 1):
    for k in range(1, i +1):
        print(k, end=" ")
    print()
for i in range(number - 1, 0, -1):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()


# 2) Receive from the user a positive number greater than 0 - and print the following form
#    *
#   ***
#  *****
# *******
# For example, if we pick up 7, print a triangle like this-
# (The base of the triangle is the number received, the apex will be 1. Each row has 2 more asterisks)

number = int(input("Please enter a positive number greater than 0: "))

for i in range(1, number + 1):
    for k in range(number -1):
        print(" ", end="")
    for h in range(2 * i -1):
        print("*", end=(""))
    print()