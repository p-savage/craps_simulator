def verify_minimum_balance(balance: int, bet_min: int) -> bool:
    """Verify the player has enough balance to cover the minimum bet.
    
    Returns True if balance is sufficient."""
    
    return balance >= bet_min
    
def inc_shooter_index(index: int, shooters: list[str]) -> int:
    """Increment to the next shooter in the shooters list.
    
    Returns the index of the next shooter in the list by wrapping to the 
    beginning of the list, if needed.""" 
    
    if index == len(shooters) - 1:
        new_index = 0
    else:
        new_index = index + 1
    return new_index
    
def verify_bet_coverage(bet: int, balance: int) -> bool:
    """Verify balance is sufficient to cover bet.
    
    Returns True if the balance is sufficient to cover the bet."""
    
    return bet <= balance
    
    