import random
from game_log import GameLog

class Craps:
    """Run the game"""
    
    def __init__(self):
        """Initialize the game"""
        self.log = GameLog()
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
            prompt = (f"\n\tShooter {self.log.shooter}, the puck is off."+
                    " Roll to establish a point.\n"+
                    "\t(Press Enter to roll or Q to quit)")
            key_press = input(prompt)
            if key_press.lower() == "q":
                self.log.update_log()
                self.game_active = False
                for i in self.log.game_log:
                    print(i)
                break
            self.dice_1,self.dice_2 = self.roll_dice()
            print(f"\nYou rolled {self.dice_1}, {self.dice_2}")
            total = self.dice_1 + self.dice_2
            self.log.inc_roll()
            if total in [7, 11]:
                print(f"Winner! {total} is an automatic win.")
            elif total in [2, 3, 12]:
                print(f'{total} craps. "Pass" line bets lose.')
            else:
                self.point = total
                off = False
                self.puck = "on"

    def puck_on(self):
        """Handle the puck on loop"""
        on = True
        while on:
            prompt = (
            f"\n\tThe point is {self.point}. Hit the point again before rolling a 7.\n"+
            "\t(Press Enter to roll or Q to quit)"
            )
            key_press = input(prompt)
            if key_press.lower() == 'q':
                self.log.update_log()
                self.game_active = False
                for i in self.log.game_log:
                    print(i)
                break
            self.dice_1,self.dice_2 = self.roll_dice()
            print(f"\nYou rolled {self.dice_1}, {self.dice_2}")
            total = self.dice_1 + self.dice_2
            self.log.inc_roll()
            if total == 7:
                print("7 craps. New shooter.")
                self.log.update_log()
                self.log.inc_shooter()
                self.log.reset_rolls()
                self.log.reset_points_hit()
                self.point = 0
                on = False
                self.puck = "off"
            elif total == self.point:
                print(
                f"{total} is a Winner! Roll again to establish a new point."
                    )
                self.log.inc_points()
                self.point = 0
                on = False
                self.puck = "off"
            else:
                print(f"{total} is not the point.")

    def roll_dice(self):
        """Simulate rolling two dice."""
        self.dice_1 = random.randint(1, 6)
        self.dice_2 = random.randint(1, 6)
        return self.dice_1, self.dice_2
        
c = Craps()
c.run_game()