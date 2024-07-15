#Exercise loops

#1. Use a loop and print all the numbers from 10 to 20:
for i in range(10, 21):
    print(i, end=" ");
print('\n')

#2. Now print all the numbers from 10 to 20 in increments of 2:
for i in range(10, 21, 2):
    print(i, end=" ");
print('\n')

#3. Now prompt a number from the user and print all the numbers from in increments of the number received. For example if the number is 3, the print will be: 10, 13, 16, 19

a: int = int(input("Please enter a number: "));
for i in range(10, 21, a):
    print(i, end=" ");
print('\n')
#4. Now prompt a number from the user for the start position, another for the end position and another one for the gap.
#please enter the starting point? 30
#please enter the end point? 47
#please enter the gap? 5
#30 40 45

a: int = int(input("Please enter the starting point: "));
b: int = int(input("Please enter the ending point: "));
c:  int = int(input("Please enter the gap: "));
for i in range(a, b, c):
    print(i, end=" ");