#4.Receive an integer from the user (int) if the number is divisible by 7 without a remainder print "seven boom" otherwise print "not seven boom ( "hint check: if the number % 7 == 0).
boom7: int = int(input("Please enter a number: "));

if  boom7 % 7 == 0:
    print("Seven boom");
else:
    print("Not seven boom")