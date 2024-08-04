# 1 Using a filter for a list of numbers:

# Create a list of 50 random numbers between 1-100 and print it:
import random

ran_list = [random.randint(1, 100) for _ in range(50)]
ran_list.sort()
print(f"The random list is: {ran_list}")

# Now use filter and lambda to get from the list:
# a. Only numbers greater than 50.

flt_lst = filter(lambda x: x < 50, ran_list) #The filter function helps create a new collection with only the items that meet a certain condition.
flt_lst = list(flt_lst)
print(f"The numbers greater than 50 are: {flt_lst}")

# b. Only numbers divisible by 7 without a remainder:

dvs = filter(lambda x: x % 7 == 0, ran_list)
dvs = list(dvs)
print(f"The numbers divisible by 7 without a remainder are: {dvs}")

# c. Only the two-digit numbers (hint: 10-99):

only_two = filter(lambda x: 10 <= x <= 99, ran_list) #It checks if the number is between 10 and 99(the 2 digit numbers of the range).
only_two = list(only_two)
print(f"The two digit numbers list is: {only_two}")

# d. Only the two-digit numbers whose ones digit is equal to their tens digit. Hint: Use % 10 and / / 10

dvsten = filter(lambda x: x % 10 // 10, ran_list) #%10 divides "x" by 10 and provides it reminder. And //10 divides "x" by 10 and rounded down to the nearest whole number.
dvsten = list(dvsten)
print(f"The 2 digit numbers module of 10 are: {dvs}")

# e. Only numbers that - the sum of their digits is 9

#option1
def sum_dig_nine(x):
    dig_sum = sum(int(digit) for digit in str(x)) #Converts #'s to a str to check over each digit and sum them.
    return dig_sum == 9 #Check if the sum of the digits is 9
filsumdignine = list(filter(sum_dig_nine, ran_list)) #Filter the list to include only numbers where the sum of digits is 9
print(f"The numbers were the sum of their digits is = 9 are: {filsumdignine}")

#option2
flsumdignine = list(filter(lambda x: sum(int(digit) for digit in str(x)) == 9, ran_list))
print(f"This is just a double check to understand better: {flsumdignine}")

# f. Only numbers larger than average

average = sum(ran_list) / len(ran_list)
print(f"The average for ran_list is: {average}")

larger_average = list(filter(lambda x: x > average, ran_list))
print(f"The numbers larger that the average are: {larger_average}")

# g. Only numbers greater than half of the maximum number in the list

maxoflist = max(ran_list)
print(f"The maximum number on the list is: {maxoflist}")

gthan_half = list(filter(lambda x: x > maxoflist / 2, ran_list))
print(f"The numbers greater than half of the maximum number are: {gthan_half}")

# h.*** Bonus: only numbers greater than the median (?)

sorted_list = ran_list.sort()

def cal_median(sorted_list): #function to check the median or middle data point of the list
    x = len(sorted_list) #calculates the number of elements on a list
    if x % 2 == 1: # To check if the number is odd
        return sorted_list[x //2] #returns the midle element of x
    else: # if x is an even number than this code will execute.
        mid1 = x // 2 - 1 #calculates the index for the first middle element
        mid2 = x // 2 #calculates the index for the second middle element
        return (sorted_list[mid1] + sorted_list[mid2]) / 2 # adds the first middle value and the second one and divide by 2  to get an average.

median = cal_median(ran_list)
print(f"The median is: {median}")

greater_median = list(filter(lambda x: x > median, ran_list))
print(f"The numbers greater that the median are: {greater_median}")