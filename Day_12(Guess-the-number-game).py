import random

HARD_LVL = 5
EASY_LVL = 10


def guess_number():
    """Guessing one number from 1 to 100"""
    return random.randint(1, 101)

def level_choice():
    """Choosing difficulty level: hard = 5 attempts, easy = """
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if answer == "hard":
        return HARD_LVL
    elif answer == "easy":
        return EASY_LVL

def hot_cold(guess_number, user_guess, turns):
    """
    Takes the user guess and compares it to the computer guess
    If you're wrong removes 1 attempt from your pool
    """
    if user_guess < guess_number:
        print("Too low")
        return turns - 1
    elif user_guess > guess_number:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it! The answer was '{guess_number}'")
        return 0


def the_game():
    """Core of the game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = guess_number()
    attemps_number = level_choice()

    while attemps_number != 0:
        print(f"You have {attemps_number} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attemps_number = hot_cold(guess_number=random_number, user_guess=user_guess, turns=attemps_number)
    continue_choice = input("Do you wanna try again? Type 'y' or 'n': ")
    if continue_choice == "y":
        the_game()
    else:
        print("Bye!")
        return

the_game()