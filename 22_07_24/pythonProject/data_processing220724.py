# Data processing:

# 1. Enter numbers until -99 is entered and display their sum.
# If -99 is entered immediately, None will be printed

t_sum = 0
while True:
    num: int = int(input("Please enter a valid number: "))
    if num == -99:
        print("There is no need to continue")
    elif sum(num):
        print(f"The total is: {t_sum} ")


# 2. Take in numbers until you take in a negative number or 0
# Show the highest and lowest value you recorded
# If -99 is entered immediately, None will be printed
# 3. Pick up 5 numbers.
# Display the serial number of the highest value.
# For example, if we receive: 12, 99, 12, 4, 5, 88
# The answer will be 4. because 99 is received in the fourth input
# 4. Take 2 numbers and print the result of their multiplication using only addition
# 5. Take 2 numbers and print the result of their multiplication using only multiplication
# 6. **Challenge: Enter a number and enter a digit and write True if the digit appears in the number and False if it does not
# appears in the number For example, if 789 and 3 are entered, then False. If we get 476 and 7 then True
# 7. **Challenge: Take 2 numbers and print their greatest common divisor
# For example, the largest divisor of 60 and 72 is: 12
# For example, the greatest divisor of 64 and 81 is: 1
# 8. A prime number is a number that is divisible by itself and only by 1
# Write a program that accepts a number and prints whether it is prime or not
# Hint: run with i from 2 to the number and check if the number % i == 0 sometime. If so, the number is not prime.
# If you didn't find one, the number is prime