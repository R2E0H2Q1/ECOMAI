# input numbers form the user
# print the max number of the input
# exit the loop got -999
number: int = 0
the_max: int = None
the_min: int = None
while True:
    number = int(input('Enter number [-999 to exit]:'))
    if number == -999:
        break

    '''#################################### MAX ############################'''
    '''############# way 1'''
    if the_max == None or number > the_max:
        the_max = number

    '''############# way 2'''
    if not the_max or number > the_max:
        the_max = number

    '''############# way 3'''
    the_max = number if not the_max or number > the_max else the_max;

    '''#################################### MIN ############################'''
    '''############# way 1'''
    if the_min == None or number < the_min:
        the_min = number

    '''############# way 2'''
    if not the_min or number < the_min:
        the_min = number

    '''############# way 3'''
    the_min = number if not the_min or number < the_min else the_min;

print(f"the min number is {the_min}")
print(f"the max number is {the_max}")

# add same logic for the minimum number
