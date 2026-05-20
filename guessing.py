import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess == secret:
        print(" Correct! You guessed it!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")