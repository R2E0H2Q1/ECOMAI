# add same logic from max number for the minimum number
number: int = 0
the_min: int = None
while True:
    number = int(input('Enter number:'));
    if number == -999:
        break
    ############# way 1
    if the_min == None or number < the_min:
        the_min = number
    print(f"the minimum number is {the_min}");