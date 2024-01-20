# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.
import random

random_number = random.randint(1, 100)
random_number = 56
while True:
    user_guess = int(input("Guess the number between 1 and 100: "))

    if user_guess == random_number:
        print(f"Congratulations! You guessed the correct number, it's a {random_number}.")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

