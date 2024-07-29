
def hello():
    print('hello')

def get_int(msg: str = 'Enter number: ', err: str = 'Something went wrong.... try again'):
    """
    This function gets an input of integer from the user
    whenever a string is received it will get it again

    Parameters:
        msg: str, default 'Enter number: '
        err: str = 'Something went wrong.... try again'

    Returns:
        integer number
    """
    num: int = None

    while not num:
        try:
            num = int(input(msg))
        except:
            print(err)
    return num

if __name__ == "__main__":
    print('testing import ...')
