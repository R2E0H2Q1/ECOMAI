
num: int = int(input('Enter number: '))
sum_digits: int = 0
while num > 0:
    rdigit: int = num % 10
    sum_digits += rdigit
    num = num // 10
print(f'digit sum = {sum_digits}')
