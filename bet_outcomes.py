class Bets:
    """Ledger for tracking bets"""
    
    def __init__(self):
        """Initialize the ledger"""
        self.pass_line_bet = None

    def pass_line_win(self, balance):
        """Increase shooter balance by the pass line bet amount
        and reset the pass line bet amount"""
        balance += self.pass_line_bet
        print(f"Bankroll: {balance}")
        self.pass_line_bet = 0
        return balance

    def pass_line_loss(self, balance):
        """Decrease shooter balance by the pass line bet amount
        and reset the pass line bet amount"""
        balance -= self.pass_line_bet
        print(f"Bankroll: {balance}")
        self.pass_line_bet = 0
        return balance