# #1 Absorb 10 numbers from the user in a loop, then print:
# a. How many positive numbers were recorded
# b. How many negative numbers were absorbed
# c. How many times has the number 0 been inserted
# d. Some numbers divisible by 7 without remainder were absorbed
# e. What would be the last positive number inserted – if there were no such Print Read More
# f. What was the last negative number inserted – if there were no such Print "None"
# g. If a number greater than 1000 or less than minus 1000 is inserted, ignore the number (hint: continue)
# h. If the number minus 9999 is inserted, then exit the loop and do not print statistics at all
# Use the else loop as we did in class


pos_num = 0
neg_num = 0
zero = 0
mod7 = 0
lastpos = None
lastneg = None
while True:
    x = int(input("Please enter a number: "));
    if x == -999:
        break
    if  x > 0:
        pos_num += 1
        lastpos = x
    if x < 0:
        neg_num += 1
        lastneg = x
    if x == 0:
        zero += 1
    if x % 7 == 0:
        mod7 += 1
    if x > 1000 or x < -1000:
        continue
    if x != -999:
        print(f"The number of positive numbers recorded is:{pos_num} !")
        print(f"The number of negative numbers recorded is:{neg_num} !")
        print(f"Zero has been typed {zero} times.")
        print(f"{mod7} are the registered numbers divisible by 7 with a modulo 0")
    if lastpos is not None:
        print(f"The last positive number is {lastpos} ");
    if lastneg is not None:
        print(f"The last positive number is {lastneg} ");
else:
    print("The party is over!")