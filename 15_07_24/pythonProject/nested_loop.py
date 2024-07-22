
# nested loop: it's a loop inside a loop
number: int = 1

# will run 3 x 5 = 15 times
for j in range(1, 4):  # 3
    for i in range(1, 6):  # 5
        print(number, end=" ")
        number += 1
    print()

# input number from user, i.e. 5
# 1
# 12
# 123
# 1234
# 12345

number: int = 9;
for i in range(1, number + 1):  # 1 2 3 4 5
    for j in range(1, i + 1):  # 1..1 1..2 1..3 1..4 1..5
        print(j, end="")
    print()