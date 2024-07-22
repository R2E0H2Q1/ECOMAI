# 2. Level B lists:
import statistics

# a. Generate an empty list of decimal numbers of temperatures and

temps: list[float] = [] #empty list with decimal numbers

# b. Enter temperatures from the user until the number minus 999 is entered for each temperature # Received add to list.
# We will not add a temperature greater than 50 or less than minus 50

while True:
    temp = float(input("Please enter a temperature(Please pres -999 to exit!): ")) #Input with decimal numbers
    if temp == -999:
        break
    if temp > 50 or temp < -50:
        print(f"The temp {temp} is outside the valid range")
        continue
    temps.append(temp)  #Adds the entered temperature to the temps list. With the exception of -999.
    print(f'Temperatures: {temp}')
print(f"The collected temperatures are: {temps}") #Prints the final list, that doesn't includes the out of range ones.

# c. Add the following list of temperatures at the end of the current list: [18.5, 39.1 -20.0] / (hint extend).
temps.extend([18.5, 39.1, -20.0]) #.extend allows to add lists at the end of other lists.
print(f"The extended list is: {temps} ")

# d. Print the highest temperature (hint max)

print(f"The highest temperature on the list is: {max(temps)} ")

# e. Print the lowest temperature (hint min)

print(f"The lowest temperature on the list is: {min(temps)} ")

# f. Print the average of the temperatures using sum and len

print(f"The lowest temperature on the list is: {min(temps)} ")

# g. Print the temperature average using mean (statistics library)
import statistics
print(f"The temperature averages is: {statistics.mean(temps)}")

# h. Remove the temperature at index 0

rem: int = temps.pop(0)
print(f" Value of index 0 was removed! {rem}")

# i. remove the temperature 18.5 (hint remove)

remtwo: int = temps.remove(18.5)
print(f" Value of index 0 was removed! {remtwo}")

# j. Extract the last temperature in the list into a memory cell called last_temp (hint pop)

last_temp: int = temps.pop(-1)
print(f"The las temperature of the list is: {last_temp}")

print(temps) #code check

# k. Duplicate the list using copy, sort the new list you created

copy_temps = temps.copy()
copy_temps.sort()

print(f"The copy of the list temps is {copy_temps}")


# l. Duplicate the list again using copy, sort the new list you created in reverse order

copy_temps = temps.copy()
copy_temps.sort(reverse=True)

print(f"The reversed copy of the list temps is {copy_temps}")


# m. What is the difference between sort and sorted

#Answer: Sorted does NOT change the list.

# n. What type does the reversed function return? How can it be made into a list?

#Answer: Returns a reversed clone of the original list.
# In order to made it into a list you need to pass it to the list().