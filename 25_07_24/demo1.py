from functions import greeting, greeting2  # list each function
#import functions  # bring all

from proj1.funcs import get_int2

print(__name__)

from functions import get_int
import functions

get_int()

#import functions
get_int()

greeting()
greeting2()

### Appendix
### how to get all of the functions name from a file
import inspect
print('======= inspect')
my_functions = inspect.getmembers(functions, inspect.isfunction)
for f in my_functions:
    print(f[0])


# open a new python file called: program.py
# open a new python file called: global_func.py
# in global_func.py: define function called hello -- print('hello')
# like this-
# def hello():
#     print('hello')
# inside global_func somewhere: add print('testing import...')
# print('testing import...')

# in program.py:
# import global_func as gf
# gf.hello()
# see if you get the 'testing import' in the console
# now add if __name__ == "__main__" with the print('testing import...') inside
# now run program again and see it does not print
