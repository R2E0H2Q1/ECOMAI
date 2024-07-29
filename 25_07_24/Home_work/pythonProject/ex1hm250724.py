# 1 Base strings:
#  will generate a (one) string of your full name and city of residence. Make sure there is a space between the names.

fullname: str = str(input(" Please enter your full name: "))
citres: str = str(input("Please enter your city of residence: "))
string: str = "I " + fullname + " " +"reside at " + citres
print(string)

# a. Print the length of the string. Hint len

print(len(string))

# b. Print the entire string in uppercase. hint upper

print(string.upper())

# c. Print the entire string in lowercase. Hint lower

print(string.lower())

# d. Check if the string starts with your first name. hint startswith

fname = fullname.split()[0]
print(string.startswith(fname))

# e. Check if the string ends in your city of residence. Hint endswith

print(string.endswith(citres))

# f. Extract the string into a list containing your first name, last name, city of residence. hint split

list = string.split()
print(list)

# g. Turn the spaces into stars. Hint replace. Then - unpack the new string again to the list (as in the previous section)

new_string = string.replace(" ", "*")
print(new_string)

# h. Print the string in the center of 50 characters, wrapped in the "=" character. Hint center

width = 50
center_string = string.center(width)
print(center_string)

# i. Print the string from the 4th character to the end

index = 4
short_string = string[index]
print(short_string)

# j. Print the string from the beginning to the 4th character (inclusive)


# k. Print all even characters in a string

even = string[::2]
print(even)

# l. Make sure each word in the string starts with a capital letter. Hint title

capital = string.title()
print(capital)