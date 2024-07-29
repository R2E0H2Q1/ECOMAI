#3. Using import:

# a. Create a file called my_func.py and insert the following function into it:
# def print_stars():
#  print('************')

# b. Create another file named main.py and inside it use Import to call the function in the file my_func.py (see code from the lesson)

import my_func

# i. Solved using import to the entire file with its normal name

from my_func import print_stars #import functions  # bring all

# ii. Solved using import to the entire file with the abbreviated name of mf. Hint as

import my_func as mf

# iii. Solve using from to import only the stars_print function

print('************')

# c. Add to my_func.py a printout of the calculation result of 10*999
# Now make sure that the print does not appear when doing import.
# if __name__ == "__main__" rem

