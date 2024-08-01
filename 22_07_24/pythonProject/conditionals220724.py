#Conditionals:

# 1. Enter two decimal numbers. Print the small one 3 times

numb1: float = float(input(f"Please enter a valid decimal number: "))
numb2: float = float(input(f"Please enter a valid decimal number: "))

smaller = min(numb1, numb2)
print(f"The smaller number is: {smaller}");
print(f"The smaller number is: {smaller}");
print(f"The smaller number is: {smaller}");
print()

# 2. Take 2 integers and print their average

avg = numb1 + numb2 / 2
print(f"The average for these integers is: {avg}")
print()

# 3. Take 3 numbers and print the largest of the three

num1: float = float(input(f"Please enter your first number: "))
num2: float = float(input(f"Please enter your second number: "))
num3: float = float(input(f"Please enter your third  number: "))

print(f"The largest of the 3 provided integers is: {max(num1, num2, num3)}")
print()

# 4. Record the length of a movie in minutes and print how many hours and minutes it is.
# For example, if we enter -105, the answer will be 1 hour(s) and 45 minute(s)

movie_time: int = int(input("How long was the movie? Please enter your response in minutes: "))
h = movie_time // 60
m = movie_time % 60

print(f"The total length for the movie was {h} hours and {m} minutes!")
print()

# 5. Enter a number, it is guaranteed that it is 4 digits long, find what the rightmost digit is and print it:

fourth: int = int(input("Please enter a 4 digits number: "))
right = repr(fourth) #repr() function returns a printable representation of the object by converting that object to a string.
print(f" The rightmost digit for the provided number is: {right[-1]}")
print()

# 6. Enter a number, it is guaranteed that it is 4 digits long, find what the second digit is from the right and print it

f_digits: int = int(input("Please enter a 4 digits number: "))
f_digits_str = str(f_digits)
if len(f_digits_str) != 4:
    print(F"The provided number is less than fourth digits!")
else:
    print(F"The second digit for the provided number is {f_digits_str[1]}")
print()

# 7. Enter a two-digit number and print the sum of its digits

two: int = int(input("Please enter a two digit valid number: "))
two_str = str(two)
if len(two_str) !=2:
    print(F"The provided number is not equal to two digits!")
else:
    digit1 = int(two_str[0])
    digit2 = int(two_str[1])
    total = digit1 + digit2
    print(f" The sum of the 2 digits you entered is: {total}")
print()

# 8. Take a two-digit number and reverse its digits. For example, if we take 61, the answer will be 16

reversed_num = two_str[::-1]
new = int(reversed_num)
print(f"The reversed number for the provided integer is: {new}")
print()

# 9. Take a number and write even if it is even and odd if it is odd

evenorodd: int = int(input("Please enter a number: "))
if evenorodd % 2 == 0:
    print("The provided number is even")
else:
    print("The number is odd")
print()

# 10. Income tax calculator.
# Collect his salary from the user and calculate how much tax he has to pay:

salary: float = float(input("Please enter your monthly salary in shekels: "))

# Income up to NIS 6,000: 0% tax.
if salary == 6000:
    print("You don't need to pay any taxes!")

# For every shekel over NIS 6,000 to NIS 12,000: 10% tax.
elif salary > 6001 and salary <= 12000:
    print(f"You need to pay: {(salary * 10) / 100} shekels")

# For every shekel from NIS 12,000 to NIS 18,000: 20% tax.
elif salary > 12001 and salary <= 18000:
    print(f"You need to pay: {(salary * 20) / 100} shekels")

# For every shekel from NIS 18,000 to NIS 25,000: 30% tax.
elif salary > 18001 and salary <= 25000:
    print(f"You need to pay: {(salary * 30) / 100} shekels")

# For every shekel from NIS 25,000 to NIS 35,000: 40% tax.
elif salary > 25001 and salary <= 35000:
    print(f"You need to pay: {(salary * 40) / 100} shekels")

# For every shekel from NIS 35,000 to NIS 50,000: 45% tax.
elif salary > 35001 and salary <= 50000:
    print(f"You need to pay: {(salary * 45) / 100} shekels")

# For every NIS over 50,000: 51% tax.
else:
    print(f"You need to pay: {(salary * 51) / 100} shekels")
print()

# 11. It is allowed to board the roller coaster from the age of 8 to 18 if your height is over 115 cm.
# Enter a person's age and height in cm and show whether the person is allowed to enter the facility.

age: int = int(input("Please enter your age: "))
height: float = float(input("Please enter your height in centimeters: "))

if 8 <= age <= 18 and height >= 115:
    print(f" You are allowed in the rollercoaster")

# After the age of 18 it is allowed to climb even if your height is only over 100 cm.
elif age > 18 and height >= 100:
    print(f" You are allowed in the rollercoaster")

else:
    print("You are either too young or too short to use this rollercoaster!!")