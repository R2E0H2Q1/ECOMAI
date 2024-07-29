# why ?
# how
def greeting():
    print('=============')
    print('Hello python')
    print("let's code")
    for i in range(10):
        print(i, end=" ")
    print()


def greeting2():
    print('=============')
    print('Hello python')
    print("let's code")
    for i in range(10):
        print(i, end=" ")
    print()


def get_int():
    num: int = None
    while not num:
        try:
            num = int(input('Enter number: '))
        except:
            print('Something went wrong.... try again')

print(__name__)

# are you running THIS file ?
if __name__ == '__main__':
    print('not in function')
    x = 1
    num = None
    while not num:
        try:
            num = int(input('Enter number: '))
        except:
            print('Something went wrong.... try again')
    print('not in function')
    greeting()
    greeting()
    ## function
    ## while loop until ok
    ##   try-except for errors
    ##     input + int()
    print('hi')

