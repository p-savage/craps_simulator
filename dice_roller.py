import random


def roll_dice() -> tuple[int, int]:
    """Simulate rolling two dice. 
    
    Returns dice values in a tuple."""
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2