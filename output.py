def roll_total_message(dice1, dice2):
    """Print the roll total message"""
    print(f"\nYou rolled {dice1}, {dice2}")

def automatic_winner_message(dice_total, bet):
    """Print automatic win message [7 or 11]"""
    print(f"Winner! {dice_total} is an automatic win."+
    f'"Pass" line pays {bet}.')

def automatic_loser_message(dice_total, bet):
    """Print automatic loss message [2, 3, 12]"""
    print(f'{dice_total} craps. "Pass" line bet loses {bet}.')

def seven_out_message(bet):
    """Print seven-out message"""
    print(f'7 craps! "Pass" line bet loses {bet}. New shooter.')

def point_hit_message(dice_total, bet):
    """Print point hit message"""
    print(f'{dice_total} is a Winner! "Pass" line pays {bet}.')

def trivial_total_message(dice_total):
    """Print trivial total message"""
    print(f"{dice_total} is not the point.")

def game_log_message(log):
    """Print game log after user-initiated quit"""
    print("\n")
    for i in log:
        print(i)
    print("\n")