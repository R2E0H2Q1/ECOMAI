#input number from user, i.e.5
#1
#12
#123
#1234
#12345

number: int = int(input("Please enter a number: "))#needs to enter 5 to get the result.
for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
