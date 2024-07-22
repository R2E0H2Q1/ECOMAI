
grade1: int = 100
grade2: int = 99
#.. 100... 1000

#                      0   1   2
grades: list[int] = [100, 92, 97]  # () {}
names: list[str] = ["danny", "moshe", "suzi"]
flags: list[bool] = [True, False, True, True]
points: list[float] = [1.99, 2.99, 0.001]
#   len = 5
#   0    1   2   3   4 (len-1)
# [99, 100, 92, 97, 88]
print(grades)
grades.append(88)
grades.insert(0, 99)
print(grades)
print(len(grades))