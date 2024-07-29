# 7 ==>
# 7 % 2 == 1
# 7 % 3 == 1
# 7 % 4 == 3
# 6 = 3 * 2
# 7 % 5 == 2
# 7 % 6 == 1
prime: bool = True
num: int = int(input('Enter number: '))
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
print(f"{num} is {'Not ' if not prime else ''}Prime")

#num: int = int(input('Enter number: '))
divided: [bool] = []
for i in range(2, num):
    is_divided: bool = num % i == 0
    divided.append(is_divided)
print(divided)
comp = [num % i == 0 for i in range(2, num)]
print(comp)
print(f"{num} is {'Not ' if any(divided) else ''}Prime")

print(f"{num} is {'Not ' if any(num % i == 0 for i in range(2, num)) else ''}Prime")
print([num % i for i in range(2, num)])
print(f"is Prime? {all([num % i for i in range(2, num)])}")

