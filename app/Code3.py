import random

def roll_dice(sides=6):
    return random.randint(1, sides)

print("Rolling a 6-sided die...")
print(f"You rolled a {roll_dice()}")