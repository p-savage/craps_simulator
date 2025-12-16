from user_input import*
from output import*
from dice_roller import roll_dice
from game_log import GameLog
from bets import Bets

class Craps:
    """Run the game"""
    
    def __init__(self):
        """Initialize the game"""
        self.log = GameLog()
        self.bets = Bets(self)
        self.point = 0
        self.puck = "off"

    def run_game(self):
        """Start the game loop"""
        self.game_active = True
        while self.game_active:
            if self.puck == "off":
                self.puck_off()
            if self.puck == "on":
                self.puck_on()

    def puck_off(self):
        """Handle the puck off loop"""
        off = True
        while off:
            
            #get a pass line bet
            pass_line_bet = pass_line_prompt(self.log.shooter)
            if not pass_line_bet:
                self.log.update_log(balance=self.bets.balance)
                self.game_active = False
                game_log_message(self.log.game_log)
                break
            else:
                self.bets.pass_line_bet = pass_line_bet
            
            #prompt the shooter for a come out roll
            come_out = come_out_prompt(self.log.shooter)
            if not come_out:
                self.log.update_log(balance=self.bets.balance)
                self.game_active = False
                game_log_message(self.log.game_log)
                break
            
            #call for the roll and increment
            dice1, dice2 = roll_dice()
            total = dice1 + dice2
            self.log.inc_roll()
            
            #print the total
            roll_total_message(dice1, dice2)
            
            #logic based upon total
            if total in [7, 11]:
                automatic_winner_message(total, self.bets.pass_line_bet)
                self.bets.pass_line_win()
            elif total in [2, 3, 12]:
                automatic_loser_message(total, self.bets.pass_line_bet)
                self.bets.pass_line_loss()
            else:
                self.point = total
                off = False
                self.puck = "on"

    def puck_on(self):
        """Handle the puck on loop"""
        on = True
        while on:
            
            #prompt to keep rolling
            roll_again = roll_again_prompt(self.point)
            if not roll_again:
                self.log.update_log(balance=self.bets.balance)
                self.game_active = False
                game_log_message(self.log.game_log)
                break
            
            #call for the roll and increment
            dice1, dice2 = roll_dice()
            total = dice1 + dice2
            self.log.inc_roll()
           
            #print the total
            roll_total_message(dice1, dice2)
            
            #logic based upon total
            if total == 7:
                #print output
                seven_out_message(self.bets.pass_line_bet)
                #process bet outcome
                self.bets.pass_line_loss()
                #update log
                self.log.update_log(balance=self.bets.balance)
                #increment shooter and reset appropriate values
                self.log.inc_shooter()
                self.bets.reset_balance()
                self.log.reset_rolls()
                self.log.reset_points_hit()
                self.point = 0
                on = False
                self.puck = "off"
            elif total == self.point:
                #print output
                point_hit_message(total, self.bets.pass_line_bet)
                #process bet outcome
                self.bets.pass_line_win()
                #update log
                self.log.inc_points()
                #reset values and flags
                self.point = 0
                on = False
                self.puck = "off"
            else:
                trivial_total_message(total)
        
c = Craps()
c.run_game()