#start

fname: str = input("What's your name?");
lname: str = input("What's your last name?");
age: float = float(input("What's your age?"));

#option 1 to print
print("Your name is", fname, lname, "your age is", age);

#option 2 to print
print(f"Your name is {fname} {lname} your age is: {age}");

#end

#     x   y
# A(8.7, 9.9)
# input str point name # A
# input float x # 8.7
# input float y # 9.9
# printf f"..."
point_name: str = input("what's the point name?");
x: float = float(input("what's the point x value?"));
y: float = float(input("what's the point y value?"));
print(f"{point_name}({x}, {y})");

#exercise to check 2 numbers.
# input x 3
# input y -2
# check which one is bigger
# printf: The numbers {smaller}, {bigger}
# The numbers: -2, 3
x: int = int(input("first number? "))
y: int = int(input("second number? "))
if x > y:
    print(f"The numbers in ascending order: {y}, {x}")
else:
    print(f"The numbers in ascending order: {x}, {y}")