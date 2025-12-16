from user_input import*
from output import*
from puck_off import PuckOff
from puck_on import PuckOn
from game_log import GameLog
from bets import Bets

class Craps:
    """Run the game"""
    
    def __init__(self):
        """Initialize the game"""
        self.log = GameLog()
        self.bets = Bets(self)
        self.point = 0
        self.puck = False
        self.game_active = True
        self.puck_off = PuckOff(self)
        self.puck_on = PuckOn(self)
   
    def run_game(self):
        """Start the game loop"""
        while self.game_active:
            if self.puck == False:
                self.puck_off.handle_come_out_cycle()
            if self.puck == True:
                self.puck_on.puck_on_cycle()
        
c = Craps()
c.run_game()