int #Los tipos enteros o int en Python permiten almacenar un valor numérico no decimal ya sea positivo o negativo de cualquier valor.

i = 12
print(i)
print(type(i)); #Prints the class of the variable(In this precise example will return 'int' as class).

x: int = int(input("Please provide a valid number: "));
print(x);

###############################################################################################################################################################
float #El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales.

x: float = 2.5
print(x);
y: float = float(input("Please provide a valid number: "));
print(y);

###############################################################################################################################################################
str # o string son un objeto de tipo inmutable(Si permiten ser modificados una vez creados), que permite almacenar secuencias de caracteres.
# Para crear una, es necesario incluir el texto entre comillas dobles ".

s = "Esto es una cadena"
print(s)       #Esto es una cadena
print(type(s)) #<class 'str'>

###############################################################################################################################################################
#Conditionals in python
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

#if: An "if statement" is written by using the if keyword.
#Es muy importante tener en cuenta que la sentencia if debe ir terminada por ":"

a = 33
b = 200
if b > a:
  print("b is greater than a")

if b != 0:
    c = a/b
    d = c + 1
    print(d)

#elif: The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

#else: The else keyword catches anything which isn't caught by the preceding conditions. You can also have else without elif.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#If Inside If: You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")




#The match case statement in Python is initialized with the match keyword followed by the parameter to be matched.
# Then various cases are defined using the case keyword and the pattern to match the parameter.
# The “_” is the wildcard character that runs when all the cases fail to match the parameter value.
# match parameter:
#     case pattern1:
#         # code for pattern 1
#     case pattern2:
#         # code for pattern 2
#
#     case patterN:
#         # code for pattern N
#     case _:
#         # default code block

day: int = int(input("Enter a day and get it in a string:"))
match day:
    case 1:
        print("Sunday");
    case 2:
        print("Monday");
    case 3:
        print("Tuesday");
    case 4:
        print("Wednesday");
    case 5:
        print("Thursday");
    case 6:
        print("Friday");
    case 7:
        print("Saturday");
    case _:#else
        print("Invalid day.");