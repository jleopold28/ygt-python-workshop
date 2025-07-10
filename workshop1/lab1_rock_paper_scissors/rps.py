# import libraries at the top of the file
import random

# setup count of user and cpu wins
user_wins = 0
cpu_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit: ")

    if user_input == "q":
        # break means to immediately exit the loop
        break

    # check user input is valid
    if user_input not in options:
        print(f"You picked {user_input}, but that is not a valid option!")
        # continue means to go back to the top of the loop
        continue
    
    # generate a random number from 0 to 2 -> (0,1,2)
    random_number = random.randint(0,2)

    # rock: 0, paper: 1, scissors: 2
    cpu_pick = options[random_number]
    print(f"Computer picked {cpu_pick}.")

    if user_input == "rock" and cpu_pick == "scissors":
        print("You win!")
        user_wins = user_wins + 1
    elif user_input == "paper" and cpu_pick == "rock":
        print("You win!")
        user_wins = user_wins + 1
    elif user_input == "scissors" and cpu_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == cpu_pick:
        print("Draw!")
        ties += 1
    else:
        print("You lost!")
        cpu_wins += 1

print(f"User Wins: {user_wins}")
print(f"CPU Wins: {cpu_wins}")
print(f"Ties: {ties}")
print("Goodbye!")
