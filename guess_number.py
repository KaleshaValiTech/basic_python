"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random

def number_guessing_game():
    random_number = random.randint(1, 20)
    guess_count = 1

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 20. You have 5 attempts.")

    while guess_count <= 5:
        try:
            user_input = int(input(f"Attempt {guess_count}: Enter your guess: "))

            if user_input < 1 or user_input > 20:
                print("Please enter a number between 1 and 20.")
                continue

            if user_input < random_number:
                print("Too Low")
            elif user_input > random_number:
                print("Too High")
            else:
                print("Correct! You guessed the number!")
                return

            guess_count += 1

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Game over! The correct number was {random_number}.")

number_guessing_game()

Example Output:-
----------------
Welcome to the Number Guessing Game!
Guess a number between 1 and 20. You have 5 attempts.
Attempt 1: Enter your guess: 10
Too Low
Attempt 2: Enter your guess: 15
Too High
Attempt 3: Enter your guess: 13
Correct! You guessed the number!
