#Write a loop that receives a pair of strings from the user and each time prints a chain of cycles
#For example, if "morning" "good" is entered, it will be printed -  good morning
#Exit the loop only if the 2 strings are the same
#Use True while, and break
while True:
    a = input("Please enter your message: ");
    b = input("Please enter your message: ");
    print(f"I hope you are having a {a} {b} day!");

    if a == b:
        break