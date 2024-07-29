def get_int2():
    num: int = None
    while not num:
        try:
            num = int(input('Enter number: '))
        except:
            print('Something went wrong.... try again')