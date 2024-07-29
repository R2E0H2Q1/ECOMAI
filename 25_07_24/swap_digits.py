
# 97 = 9 * 10 + 7
# 97 % 10 = 7 ==> 7 * 10 = 70
# 97 // 10 = 9 ==> 70 + 9 = 79
# 79 = 7 * 10 + 9

#    97
# 0 ___
#   100

num = int(input('enter number: '))
rdigit: int = num % 10
ldigit: int = num // 10
new_number: int = rdigit * 10 + ldigit
print(f"{num} ==> {new_number}")

