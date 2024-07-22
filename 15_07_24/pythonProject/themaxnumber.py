# input numbers form the user
# print the max number of the input
# exit the loop got -999

number: int = 0
count: int = 0
the_max: int = None
while True:
    number = int(input('Enter number:'))
    if number == -999:
        break
    ############# way 1
    if the_max == None or number > the_max:
        the_max = number
    ############# way 2
    if not the_max or number > the_max:
        the_max = number
    ############# way 3
    the_max = number if not the_max or number > the_max else the_max;

print(f"the max number is {the_max}")

# add same logic for the minimum number
