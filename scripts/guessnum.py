# guessing_game.py

import random  # module built-in allows us to generate random numbers

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

#randint get it to choose a number 

# Ask the user to guess until they get it right
while True: 
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Ta-dah!! Mind-reader!")
        break
    elif guess > secret_number:
        print("Booo too high!")
    else: 
            print("Booo too low!")
