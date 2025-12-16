import random

def roll_dice():
        """Simulate rolling two dice."""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2