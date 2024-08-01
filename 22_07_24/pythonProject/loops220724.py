# Loops:

# 1. Input a natural number (positive integer) top. Display all natural numbers from 1 to top (inclusive).

top: int = int(input("Please enter a number: "))
for all in range(1, top + 1):
    print(all, end=" ")
print()
print()

# 2. Take two integers and display all the integers between them (including) in ascending order.
# It is not guaranteed that the second figure is greater than the first.

int1: int = int(input("Please enter a number: "))
int2: int = int(input("Please enter a number: "))

ascending_list = []

ini = min(int1, int2)
fin = max(int1, int2)

for int_all in range(ini, fin + 1):
    ascending_list.append(int_all)
    print(int_all, end=" ")
print()
print()

# 3. Input a natural number n.
n: int = int(input("Please enter a natural number: "))
print(n)

# Display all even numbers from 0 to n (inclusive). n is not guaranteed to be even.
for all_even in range(0, n + 1):
    if all_even % 2 == 0:
        print( all_even, end=" ")
print()

# 4. Enter two natural numbers max and den.
# Display all natural numbers up to and including max (which are divisible by den.
# It is not guaranteed that max itself is divisible by den.

max: int = int(input("Please enter a number: "))
den: int = int(input("Please enter a number: "))

for numbers in range(1, max + 1):
    if numbers % den == 0:
        print(f"The numbers are: {numbers}")

else:
    print(f"The numbers are not divisible")