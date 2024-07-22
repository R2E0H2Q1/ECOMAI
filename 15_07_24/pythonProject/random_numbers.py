# print 6 random numbers between 1-45

import random  # bring this module into my program
# from random import randint # import only a function

for i in range(1, 7):
    rnd: int = random.randint(1, 45)  # random between 1-45 (include 45)
    print(rnd, end=" ")

# nosaf
print()
nosaf: int = random.randint(1, 6)  # random between 1-6
print(f'mispar nosaf = {nosaf}')

random_bool: bool = random.choice([True, False])
random_name: str = random.choice(["Danny", "Yossi", "Shlomi"])
#100 * random.random() # 0.0 -- 1.0
#random.uniform(9.9, 12.1)

# run it in a loop until the user answers correctly..
# random an int number between 1-100 (num1) 40
# random an second int number between 1-100 (num2) 100
# print an exercise num1 + num2 = ?
#                     40 + 100 = ? 140
# ask input from the user
# check if the user answered correctly
number1: int = random.randint(1, 100)  # random number between 1-100
number2: int = random.randint(1, 100)  # random number between 1-100
print(f"{number1} + {number2} = ?")
correct_result: int = number1 + number2
while True:
    user_answer: int = int(input("What's the result?"))
    if user_answer == correct_result:
        break
    else:
        print(f"Wrong. the answer is not {user_answer}. the correct answer is {correct_result}")

print(f"Correct! the answer is {correct_result}")






