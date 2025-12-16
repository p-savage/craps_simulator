from user_input import*
from output import*
from dice_roller import roll_dice

class PuckOn:
    """Class to handle puck on cycle"""
    
    def __init__(self, craps):
        """Initialize puck on attributes"""
        self.craps = craps  
    
    def puck_on_cycle(self):
        """Handle the puck on loop"""
        
        while self.craps.puck:
            
            #prompt to keep rolling
            roll_again = roll_again_prompt(self.craps.point)
            if not roll_again:
                self.craps.log.update_log(balance=self.craps.bets.balance)
                self.craps.game_active = False
                game_log_message(self.craps.log.game_log)
                break
            
            #call for the roll and increment
            dice1, dice2 = roll_dice()
            total = dice1 + dice2
            self.craps.log.inc_roll()
            
            #print the total
            roll_total_message(dice1, dice2)
            
            #logic based upon total
            if total == 7:
                #print output
                seven_out_message(self.craps.bets.pass_line_bet)
                #process bet outcome
                self.craps.bets.pass_line_loss()
                #update log
                self.craps.log.update_log(balance=self.craps.bets.balance)
                #increment shooter and reset appropriate values
                self.craps.log.inc_shooter()
                self.craps.bets.reset_balance()
                self.craps.log.reset_rolls()
                self.craps.log.reset_points_hit()
                self.craps.point = 0
                self.craps.puck = False
            elif total == self.craps.point:
                #print output
                point_hit_message(total, self.craps.bets.pass_line_bet)
                #process bet outcome
                self.craps.bets.pass_line_win()
                #update log
                self.craps.log.inc_points()
                #reset values and flags
                self.craps.point = 0
                self.craps.puck = False
            else:
                trivial_total_message(total)