
x: int = None
while not x:
    try:
        print(1)
        x = int(input('number?'))
        break
    except:
        print(4)
        print('something went wrong...')
    print(5)

x = x + 1

print('do it please...')