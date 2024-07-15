boom7: int = int(input("Please enter a number: "));

if boom7 % 7 == 0:
    print("Seven boom");
else:
    print("Not seven boom")

#option #2
if boom7 % 7 != 0:
    print("not")
print("seven boom");

#option 3
if not boom7 % 7 != 0:
    print("not", end=" ")
print("seven boom");

#option 4
if not boom7 % 7 == 0:
    print("not", end=" ")
print("Not" if not boom7 % 7 == 0 else "", "seven boom");