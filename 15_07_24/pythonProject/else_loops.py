# input 10 numbers from the user
# if the user entered 10 numbers then print the avg
# if the user want to cancel he shall input the number -999
the_sum: int = 0
number: int = 0
for i in range(1, 11):
    number = int(input('enter number: '))
    if number == -999:
        break  # exit the loop
    the_sum += number
else:
    # code that will run only if Break did not happen
    # break did NOT happen
    print('all 10 numbers were inserted')
    avg: float = the_sum / 10
    print(f"the avg is: {avg: .2f}")

# jump point
print('finish')