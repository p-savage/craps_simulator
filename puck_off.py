from user_input import*
from balance_verification import*
from output import*
from dice_roller import roll_dice

class PuckOff:
    """Class to handle puck-off cycle"""

    def __init__(self,craps):
        """Initialize the puck off attributes"""
        self.craps = craps

    def come_out_cycle(self):
        """Handle the puck off loop"""
        while not self.craps.puck:
            
            #get a pass line bet
            pass_line_bet = pass_line_prompt(self.craps.shooter)
            if not pass_line_bet:
                self.craps.log.update_log(
                    shooter = self.craps.shooter,
                    balance = \
                        self.craps.table[self.craps.shooter].get("Balance"),
                    )
                self.craps.game_active = False
                game_log_message(self.craps.log.game_log)
                break
            
            #verify the shooter has enough balance to cover the bet
            valid_bet = verify_bet_coverage(
            pass_line_bet,
            self.craps.table[self.craps.shooter].get("Balance"),
            )       
            if valid_bet:
                #store the bet
                print(pass_line_bet)
                self.craps.bets.pass_line_bet = pass_line_bet
            else:
                insufficient_balance_message(
                    self.craps.table[self.craps.shooter]["Balance"]
                )
                continue
            
            #prompt the shooter for a come out roll
            come_out = come_out_prompt(self.craps.shooter)
            if not come_out:
                self.craps.log.update_log(
                    shooter = self.craps.shooter,
                    balance = \
                        self.craps.table[self.craps.shooter].get("Balance"),
                    )
                self.game_active = False
                game_log_message(self.craps.log.game_log)
                break
            
            #call for the roll and increment
            dice1, dice2 = roll_dice()
            total = dice1 + dice2
            self.craps.log.inc_roll()
            
            #print the total
            roll_total_message(dice1, dice2)
            
            #logic based upon total
            if total in [7, 11]:
                automatic_winner_message(total, self.craps.bets.pass_line_bet)
                self.craps.table[self.craps.shooter]["Balance"] = \
                    self.craps.bets.pass_line_win(
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance")
                )
            elif total in [2, 3, 12]:
                automatic_loser_message(total, self.craps.bets.pass_line_bet)
                self.craps.table[self.craps.shooter]["Balance"] = \
                    self.craps.bets.pass_line_loss(
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance")
                )
            else:
                self.craps.point = total
                self.craps.puck = True