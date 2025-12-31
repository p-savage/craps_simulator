def verify_shooter_balance(balance):
    """Verify the shooter's balance"""
    pass_line_minimum = 15
    if balance < pass_line_minimum:
        return False
    else:
        return True
    
def inc_shooter_index(shooter, shooters):
    """Increment to the next shooter index""" 
    index = shooters.index(shooter)
    if shooter == shooters[-1]:
        new_index = 0
    else:
        new_index = index + 1
    return new_index
    
def verify_bet_coverage(bet, balance):
    """Verify balance is sufficient to cover bet"""
    if bet > balance:
        return False
    else:
        return True
    
    