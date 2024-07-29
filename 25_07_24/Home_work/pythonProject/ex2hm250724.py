# Part 2 - Strings:

# a. Remove the spaces from both sides of the following string: "day-fun"

string1: str = str(" fun-day ")
nospace_str = string1.replace(" ", "")
print(nospace_str)

# b. Check if the string "hello" contains only letters. Hint isalpha

###isalpha() method is used to check if all characters in a string are alphabetic.###
###This method validates input or ensuring that a string contains only letters.###

x: str = str("hello")
onle = x.isalpha()
print(onle)

# c. Check if the string "777" contains only numbers. hint isdigit

n: str = str("777")
onnu = n.isdigit() ###check if a string represents a numeric value/Returns True if all characters in the string are digits.###
print(onnu)

# d. Check if the string " " contains only spaces. Hint isspace

y: str = str(" ")
onsp = y.isspace() ###Is used to check if all characters in a string are whitespace###
print(onsp)

# e. For the list ['A ','J ','N ','I ','N['. Create one string from it. Hint join

list = ['A ','J ','N ','I ','N']
print(list)

newstring = " ".join(list) ###concatenates elements of a list into a string.###
print(newstring)

# f. For the same list - create one string with '*' between the characters. A*J*N*I*N. Hint join

start = "*".join(list)
print(start.replace(" ", ""))

# g. Ignoring upper and lower case letters: check if the letter e appears in the word hELLo: Hint in, lower

st = "hELLo"
lowcase = st.lower()
print(lowcase)
e = "e"
if e in lowcase:
    print(F'The letter {e} does appears on the string {st}')
else:
    print(f'The letter {e} isn`t part of the string')

