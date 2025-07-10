import random

# Ask the user to input a number, this will be the max number in our range
max_number = input("Type the max number you can guess: ")

# First check if the input is a number
# inputs are strings so we must convert to int
if max_number.isdigit():
    max_number = int(max_number)

    # check number is greater than 0
    if max_number <= 0:
        print("Please type a number larger than 0 next time!")
        # exit program
        quit()
else:
    print("Error: You must input a number!")
    quit()

secret_number = random.randint(0, max_number)
guesses = 0

# while loop to play game until number is guessed
# keywords:
#   continue -> top of loop
#   break    -> exit loop
while True:
    # keep track of number of guesses
    guesses = guesses + 1

    user_guess = input("Guess the number: ")

    if user_guess == "q":
        # break means to immediately exit the loop
        break

    # input validation
    # make sure input is digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Error: Please input a number next time!")
        # continue takes us to TOP of loop
        continue

    if user_guess == secret_number:
        print("You got it!")
        # break out of loop when you guess correctly
        break
    else:
        print("Sorry, you got it wrong!")

        # tell user if they were above or below number
        if user_guess > secret_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

print(f"You got it in {guesses} guesses.")