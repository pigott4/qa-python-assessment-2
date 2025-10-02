# dice_roller.py

import random

max_rolls = random.randint(1, 6)  # dice will allow 1-6 rolls
rolls_done = 0

def roll_dice():
    return random.randint(1,6)


while rolls_done < max_rolls:
    input("Press enter to roll the dice...")
    result = roll_dice()
    print("You rolled a", result)
    rolls_done += 1

print("No more rolls!")
