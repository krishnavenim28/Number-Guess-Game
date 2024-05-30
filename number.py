import random
import time

def intro():
    global name  # Declare name as a global variable to use it outside this function
    print("May I ask you for your name?")
    name = input().strip()  # Strips any leading/trailing whitespace
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    global number  # Declare number as a global variable to use it outside this function
    number = random.randint(1, 200)
    guesses_taken = 0

    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ").strip()

        try:
            guess = int(enter)

            if 1 <= guess <= 200:
                guesses_taken += 1

                if guess < number:
                    print("The guess of the number that you have entered is too low.")
                elif guess > number:
                    print("The guess of the number that you have entered is too high.")
                else:
                    print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
                    return

                if guesses_taken < 6:
                    time.sleep(0.5)
                    print("Try Again!")

            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200.")

        except ValueError:
            print(f"I don't think that '{enter}' is a number. Sorry.")

    print(f'Nope. The number I was thinking of was {number}.')

def play_game():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        intro()
        pick()
        print("Do you want to play again? (yes or no)")
        play_again = input().strip().lower()

play_game()
