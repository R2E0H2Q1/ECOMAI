#print all the numbers between 1-100, don't print numbers which are a multiple of 7.
#sum all of the numbers (which are not multiple of 7)


total: int = 0
for i in range(1, 101):
    if i % 7 == 0:
        continue
        print(i, end=" ");
    total += i;
    print(total, end=" ");


