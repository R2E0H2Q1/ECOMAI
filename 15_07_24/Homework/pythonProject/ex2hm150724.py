# 2 Welcome to the guessing game!!
# Draw a lucky number between 1-100, hint randint
# Enter a number from the user until the user guesses the number drawn by the computer
# If a number larger than the number drawn was entered, print: big too is your number
# If a number smaller than the number drawn was entered, print: small too is your number
# If exactly the drawn number was entered, print: BINGO and exit the loop
# ** Note: The number is not drawn in each re-guess. The number is initially drawn once.
#  Before the start of the (current) game and the user tries to guess again and again until he hits**
# At the end of the game (after the player has guessed the lucky number), print how many attempts there were
# Now include the game: add an option for the user to play again until they choose to quit.
# That is - at the end of each game (after the player has guessed the lucky number) - ask the user if he wants play again?
# If he answered "yes" then the game loop will happen again (and a new number will also be drawn), if he chose no It will exit the loop.
# Hint: [program structure]
# Outer loop ..until the user chooses to exit
#  The lottery numbers
#  The game loop ...until the user guessed correctly
#  guess number etc
#  Print how many attempts there were
#  Ask the user if they want to play again? If not - get out of the loop...
# Thought question: Is it possible that when the user enters the number 99999 he will exit the 2 loops? how?
import random

number: int = random.randint(1, 100)
exit: int = 101
while True:
    drawn_num: int = int(input(f"Please enter your lucky number(To escape the game press 101): "))
    if number == drawn_num:
        print("BINGO")
        go_again = input("Do you want play again? (yes/no)")
        if go_again == "yes":
            continue
        if go_again != "yes":
            print("Thanks for playing!")
        break
    if drawn_num > number:
        print("Your number is too big!")
    if drawn_num < number:
        print("Your number is too small!")
    if drawn_num == 101:
        print("GAME OVER")
        break
