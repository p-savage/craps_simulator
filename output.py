def welcome_message() -> None:
    """Print the welcome message."""

    print("\nWelcome to the craps table. Who are our players?")

def invalid_name_message() -> None:
    """Print the invalid name entry message."""

    print("Invalid entry. Each player name must be unique.")

def roll_total_message(dice1: int, dice2: int) -> None:
    """Print the roll total message."""

    print(f"\nYou rolled {dice1}, {dice2}")

def automatic_winner_message(dice_total: int, bet: int) -> None:
    """Print automatic pass line win message."""
    
    print(
        f"Winner! {dice_total} is an automatic win."
        f" Pass line pays {bet}."
    )

def automatic_loser_message(dice_total: int, bet: int) -> None:
    """Print automatic pass line loss message."""
    
    print(f"{dice_total} craps. Pass line bet loses {bet}.")

def updated_balance_message(balance: int) -> None:
    """Print a message displaying the updated balance."""

    print(f"Bankroll: {balance}")

def seven_out_message(bet: int) -> None:
    """Print seven-out message."""
    
    print(f"7 out! Pass line bet loses {bet}. New shooter.")

def point_hit_message(dice_total: int, bet: int) -> None:
    """Print point hit message."""
    
    print(f"{dice_total} is a Winner! Pass line pays {bet}.")

def trivial_total_message(dice_total: int) -> None:
    """Print trivial total message."""
    
    print(f"{dice_total} is not the point.")

def game_log_message(log: list[str]) -> None:
    """Print game log entries sequentially."""
    
    print("\n")
    for entry in log:
        print(entry)
    print("\n")

def skip_shooter_message(shooter: str) -> None:
    """Print shooter being skipped message."""
    
    print(f"\n{shooter} doesn't have the minimum bet amount. New shooter.")

def insufficient_balance_message(balance: int) -> None:
    """Print insufficient balance message."""
    
    print(f"\nInsufficient balance. Current bankroll: {balance}")

def end_game_message() -> None:
    """Print end game message."""
    
    print("No shooter meets the pass line minimum. Game Over :(")