#Take 2 whole numbers and print them in ascending order (hint: the help in the previous section)
#If, for example, the numbers 10 and 1 are received, it will be printed: 1, 10.
#If, for example, the numbers 6 and 19 are received, it will be printed: 6, 19.
#If the numbers are the same, the 2 numbers will be printed (the order does not matter)

#Start
x : int = int(input("Please enter a number: "));
y : int = int(input("Please enter another number: "));
if x > y:
    print(y, ",", x);
if y > x:
    print(x, ",",y);
if x == y:
    print("The order doesn't matter, numbers are equal!");
#End