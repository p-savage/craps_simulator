from user_input import*
from balance_verification import*
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
                self.craps.log.update_log(
                    shooter = self.craps.shooter,
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance"),
                    )
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
                self.craps.table[self.craps.shooter]["Balance"] = \
                    self.craps.bets.pass_line_loss(
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance"),
                )
                #update log
                self.craps.log.update_log(
                    shooter = self.craps.shooter,
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance"),
                    )
                #increment shooter and verify sufficient balance
                current_shooter = self.craps.shooter
                anchor_index = self.craps.shooters.index(current_shooter)
                candidate_index = inc_shooter_index(
                    shooter = self.craps.shooters[anchor_index],
                    shooters = self.craps.shooters                    
                    )
                loop_try_counter = 0
                while loop_try_counter < len(self.craps.shooters):

                    next_potential_shooter = self.craps.shooters[candidate_index]
                    if verify_shooter_balance(
                        self.craps.table[next_potential_shooter]["Balance"]
                    ):
                        self.craps.shooter = next_potential_shooter
                        break
                    else:
                        skip_shooter_message(next_potential_shooter)
                        candidate_index = inc_shooter_index(
                            shooter = self.craps.shooters[candidate_index],
                            shooters = self.craps.shooters
                        )
                    loop_try_counter += 1
                if loop_try_counter == len(self.craps.shooters):
                    end_game_message()
                    game_log_message(self.craps.log.game_log)
                    self.craps.puck = False
                    self.craps.game_active = False

                #reset appropriate values
                self.craps.log.reset_rolls()
                self.craps.log.reset_points_hit()
                self.craps.point = 0
                self.craps.puck = False
            elif total == self.craps.point:
                #print output
                point_hit_message(total, self.craps.bets.pass_line_bet)
                #process bet outcome
                self.craps.table[self.craps.shooter]["Balance"] =\
                    self.craps.bets.pass_line_win(
                    balance = \
                    self.craps.table[self.craps.shooter].get("Balance"),
                )
                #update log
                self.craps.log.inc_points()
                #reset values and flags
                self.craps.point = 0
                self.craps.puck = False
            else:
                trivial_total_message(total)