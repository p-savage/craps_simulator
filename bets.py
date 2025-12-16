class Bets:
    """Ledger for tracking bets"""
    
    def __init__(self,craps):
        """Initialize the ledger"""
        self.log = craps.log
        self.pass_line_bet = None
        self.balance = 0

    def pass_line_win(self):
        """Increase shooter balance by the pass line bet amount
        and reset the pass line bet amount"""
        self.balance += self.pass_line_bet
        print(f"Bankroll: {self.balance}")
        self.pass_line_bet = 0

    def pass_line_loss(self):
        """Decrease shooter balance by the pass line bet amount
        and reset the pass line bet amount"""
        self.balance -= self.pass_line_bet
        print(f"Bankroll: {self.balance}")
        self.pass_line_bet = 0

    def reset_balance(self):
        """Reset the balance for a new shooter"""
        self.balance = 0