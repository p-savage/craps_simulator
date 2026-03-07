def pass_line_win(bet: int, balance: int) -> int:
    """Increase balance by the bet amount.
    
    Returns the updated player balance."""
    
    balance += bet
    return balance

def pass_line_loss(bet: int, balance: int) -> int:
    """Decrease balance by the bet amount.
    
    Returns the updated player balance."""
    
    balance -= bet
    return balance