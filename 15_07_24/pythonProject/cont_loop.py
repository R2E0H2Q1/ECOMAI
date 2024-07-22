# input grades from the user
# until got grade 999
# if the user miswritten grade not between 0-100 then ignore

grade: int = 0
the_sum: int = 0
count: int = 0
while True:
    grade = int(input('Enter grade:'))
    if grade == 999:
        break
    if grade < 0 or grade > 100:
        continue  # jump to While (True)
    the_sum += grade
    count += 1
    # if 0 >= grade >= 100:
    #     # the_sum = the_sum + grade
    #     the_sum += grade
    #     count += 1;

print(f"the avg is {the_sum / count:.2f}")

# print all the numbers between 1-100 , don't print numbers which are multiple of 7
# sum all of the numbers (which are not multiple of 7) and print it
# 1,2,3,4,5,6, 8,9,10,11,12,13, 15,

total: int = 0
for i in range(1, 101):
    if i % 7 == 0:
        continue
    if i % 40 == 0:
        print()
    print(i, end=" ")
    total += i
print()
print(f"total = {total}")


