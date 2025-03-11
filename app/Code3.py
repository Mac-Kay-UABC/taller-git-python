import random

def roll_dice(sides=20):
    return random.randint(1, sides)

print("Rolling a 20-sided die...")
print(f"You rolled a {roll_dice()}")
