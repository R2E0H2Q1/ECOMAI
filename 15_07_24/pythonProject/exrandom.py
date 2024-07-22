#run it in a loop until the user answers correctly
# random an int number between 1-100 (num1)
# random a second int number between 1-100 (num2)
# print an exercise num1 + num2 = ?
#                     40 + 100 = ? 140
# ask input from the user
# check if the user answered correctly

import random
num1: int = random.randint(1, 100);
num2: int = random.randint(1, 100);
print(num1 + num2);
correct_answer: int = num1 + num2
while True:
    user_answer: int = int(input("What's the result?"));
    if user_answer == correct_answer:
        break
    else:
        print(f"Wrong. the answer is not {user_answer}. the correct answer is {correct_answer}")

        print(f"Correct! the answer is {correct_answer}")





