# 3 Using the map. Source number:
# Create a list of 20 random numbers between minus 50 and plus 50 and print it
import random

ran_list = [random.randint(-50, 50) for _ in range(20)]
ran_list.sort()
print(f"The new 20 numbers list is: {ran_list}")

# Use map and lambda to get a new list that will contain:
# a. Any number to the power of 3

print("The numbers with exponentiation 3 are: ", list(map(lambda x: x ** 3, ran_list)))

# b. Only the unity digit of each number. Led and gamma the number 42 will become 2. Hint % 10

print("The unity digits are: ", list(map(lambda x: 1 if x % 10 == 0 else 0, ran_list))) #Returns 1 if the last digit is 0, otherwise returns 0.

# c. Any number in Fahrenheit. That is, multiply by 9/5 and add 32

print("The Fahrenheit numbers are: ", list(map(lambda x: round(x * 9/5 + 32, 2), ran_list))) #round reduces the decimals to only 2 digits.

# d. Every positive number will become the word "positive" and every negative number will become the word - "negative"

neg_pos = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero" #If x > 0 print "positive" if <0 "negative"
true_false_lst = list(map(neg_pos, ran_list))
print(f"The positive and negative list is: {true_false_lst}")

# e. The largest number will be replaced by the word "max" and the smallest by the word "min". The rest will remain the same

maxnum = max(ran_list) #To check for the max number
minum = min(ran_list) #To check for the min number

maxmincheck = list(map(lambda x: "max" if x == maxnum else "min" if x == minum else x, ran_list)) #
print(f" The Max and min numbers are: {maxmincheck}")