#Use a while loop and record integer values until a value less than 30 or greater than 300 is recorded.
#These values represent the IQ of the control group before the studies
#Calculate and print the average IQ of the group
#Then ... let's say a year of Python studies has passed ... print a message as you wish
#For example - print("one year of python training has been completed...")
#Now write another loop again (following the previous loop and the print message) and in it enter whole values
#Until a value less than 30 or greater than .300 is recorded
#These values represent the IQ of the control group after school
#Calculate and print the new average IQ of the group
#Calculate and print how much the average increased

total = int = 0;
numb_of_entries: int = 0;

while True:
    iq = float(input("Please enter your I.Q! "));
    total = total + iq;
    numb_of_entries = numb_of_entries + 1;
    if iq < 30 or iq > 300:
        break

avg: float = iq / numb_of_entries;
print(f"The average IQ in the group is {avg} ");

