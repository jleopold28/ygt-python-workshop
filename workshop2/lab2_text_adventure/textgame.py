# Import Libraries at the top
import time
import random

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    # time.sleep(1) will pause for 1 second
    time.sleep(1)

    name = input("What is your name? ")
    print(f"Hello {name}! Are you ready for an adventure?")
    play = input("Type yes or no: ")

    # if play is NOT equal to "yes", exit game
    if play != "yes":
        return
    
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    choose_path()

def choose_path():
    print("Choose your path:")
    print("1. Enter the cave.")
    print("2. Walk away.")

    # Ask user to choose path 1 or path 2
    choice = input("Enter 1 or 2: ")
    
    # Path 1: enter the cave
    # Path 2: walk away
    if choice == "1":
        enter_cave()
    elif choice == "2":
        walk_away()
    else:
        print("Not a valid choice. Try again.")
        choose_path()

def enter_cave():
    # describe the cave
    print("You enter the dark cave and hear mysterious sounds.")
    time.sleep(1)
    
    # player meets a creature
    print("As you venture deeper, you encounter a creature blocking your path.")
    time.sleep(1)

    print("The creature looks dangerous. What will you do?")
    print("1. Fight.")
    print("2. Flee.")

    # choose to fight or flee
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        combat()
    elif choice == "2":
        flee()
    else:
        print("Invalid choice. Try again.")
        enter_cave()

def walk_away():
    # player walks away
    print("You decide not to enter the cave and continue your journey elsewhere.")
    time.sleep(1)
    print("Thanks for playing!")

def combat():
    # create a basic turn based combat function
    print("You choose to fight the creature.")
    time.sleep(1)

    # define player health as 100
    # define creature health as random between 50 and 100
    player_health = 100
    creature_health = random.randint(50, 100)

    # while player and creature alive, fight
    while player_health > 0 and creature_health > 0:
        print("\nPlayer Health:", player_health)
        print("Creature Health:", creature_health)
        print("1. Attack.")
        print("2. Defend.")

        # player can attack or defend
        player_choice = input("Enter 1 or 2: ")

        if player_choice == "1":
            attack_damage = random.randint(10, 20)
            creature_health -= attack_damage
            print(f"You deal {attack_damage} damage to the creature.")
        elif player_choice == "2":
            defend_bonus = random.randint(5, 10)
            player_health += defend_bonus
            print(f"You defend and gain {defend_bonus} health.")
        else:
            print("Invalid choice. Try again.")

        if creature_health > 0:
            creature_attack_damage = random.randint(8, 15)
            player_health -= creature_attack_damage
            print(f"The creature attacks and deals {creature_attack_damage} damage to you.")

    if player_health > 0:
        print("You defeated the creature! Congratulations!")
    else:
        print("You were defeated by the creature. Game over.")

def flee(): 
    # describe flee action
    print("You choose to flee from the creature.")
    time.sleep(1)
    print("You manage to escape and continue your journey.")
    time.sleep(1)
    # exit game
    print("Thanks for playing!")

if __name__ == "__main__":
    introduction()

    