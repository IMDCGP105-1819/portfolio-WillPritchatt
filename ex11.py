import random

low = int(input("Enter lowest value: "))
high = int(input("Enter highest value: "))
to_guess = random.randint(low, high)
user_guess = low - 1
guesses = 0

while user_guess != to_guess:
    user_guess = int(input("Enter number to guess: "))
    guesses += 1
    if user_guess == to_guess:
        print("You are correct!")
    elif user_guess > to_guess:
        print("Your guess is too high!")
    elif user_guess < to_guess:
        print("Your guess is too low!")

print("It took you {} guesses".format(guesses))