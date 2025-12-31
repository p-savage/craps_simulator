from user_input import*
from output import*
from puck_off import PuckOff
from puck_on import PuckOn
from game_log import GameLog
from bet_outcomes import Bets

class Craps:
    """Run the game"""
    
    def __init__(self):
        """Initialize the game"""
        self.table = {
            "Shooter 1" : {
                "Balance" : 50,
            },
            "Shooter 2" : {
                "Balance" : 50,
            },
            "Shooter 3" : {
                "Balance" : 50,
            },
            "Shooter 4" : {
                "Balance" : 50,
            },
            "Shooter 5" : {
                "Balance" : 50,
            },
            "Shooter 6" : {
                "Balance" : 50,
            },
            "Shooter 7" : {
                "Balance" : 50,
            },
            "Shooter 8" : {
                "Balance" : 50,
            },
        }
        self.shooters = list(self.table)
        self.shooter = self.shooters[0]
        self.point = 0
        self.puck = False
        self.game_active = True
        self.log = GameLog()
        self.bets = Bets()
        self.puck_off = PuckOff(self)
        self.puck_on = PuckOn(self)
        
    def run_game(self):
        """Start the game loop"""
        while self.game_active:
            if self.puck == False:
                self.puck_off.come_out_cycle()
            if self.puck == True:
                self.puck_on.puck_on_cycle()
        
c = Craps()
c.run_game()