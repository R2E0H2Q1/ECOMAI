#To add only the number of decimals you want.
pi: float = 3.14159;
print(f"pi: {pi}");
print(f"pi: {pi:2f}");

#To adjust data in a table arragment
name1: str = "Laura Croft";
age1: int = 27;
name2: str = "Robert Croft";
age2: int = 37;

print(f"Name {name1} {age1}");
print(f"Name {name2} {age2}")


## if, else, if else(elif)

#read number from user,
#print positive, negative or zero

number: int = int(input("Enter a number: "));

if number > 0:
    print(f"{number} is Positive");
elif number < 0:
    print(f"{number} is Negative");
else:
    print(f"{number} is Zero");



