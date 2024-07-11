#5. Receive an integer from the user (int) if the number is divisible by 5 without a remainder print "Fizz", if the number is divisible by 3 with no remainder print "Buzz".
#If the number is divisible by both 3 and 5 without a remainder print "Buzz Fizz"(Hint check if the number %5 == 0, check if the number %3 == 0).

x: int = int(input("Please enter a number: "));

if x % 5 == 0 and x % 3 == 0:
    print("Buzz Fizz");

elif x % 5 == 0:
    print("Fizz");

elif x % 3 == 0:
    print("Buzz");

else:
    print("Invalid Number!");
#end
