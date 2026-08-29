import balance_verification as verify
import bet_outcomes as bet
import config_constants as cc
import dice_roller as dice
import output as out
import user_input as user
from game_log import GameLog


class Craps:
    """Class to contain the craps table simulator and its associated 
    methods. Hosts and manages game state, handles game phase loops, 
    resolves roll outcomes, and logs game information."""
    
    def __init__(self) -> None:
        """Initializes the simulator attributes."""

        self.max_players: int = cc.MAX_PLAYERS
        self.min_players: int = cc.MIN_PLAYERS
        self.name_char_limit: int = cc.CHAR_LIMIT
        self.bank_min: int = cc.BANKROLL_MIN
        self.bank_max: int = cc.BANKROLL_MAX
        self.table: dict[str, int] 
        self.shooters: list[str] 
        self.table, self.shooters = self._construct_table(
            player_max=self.max_players,
            player_min=self.min_players,
        )
        self.shooter: str = self.shooters[0]
        self.point: int = 0
        self.puck_on: bool = False
        self.game_active: bool = True
        self.log: GameLog = GameLog()
        self.pass_line_min: int = cc.PASS_LINE_MIN
        self.pass_line_max: int = cc.PASS_LINE_MAX
        self.pass_line_bet: int = 0
        self.auto_winners: tuple[int, ...] = cc.PASS_LINE_WINNERS
        self.auto_losers: tuple[int, ...] = cc.PASS_LINE_LOSERS

    def _construct_table(
            self, 
            player_max: int,
            player_min: int,
        ) -> tuple[dict[str, int], list[str]]:
        """Prompt user for player names and starting bankrolls. 
        
        Enforces a table limit for min/max players. Returns a tuple 
        containing a dict with name: bankroll pairs and a list of player 
        names used in determining shooter rotation."""
        
        table: dict[str, int] = {}
        shooters: list[str] = []
        out.welcome_message()
        while len(shooters) < player_max:
            prompt_n = "\n\tEnter player name or enter 'F' to finish: "
            try:
                name = user.player_name(
                    prompt=prompt_n,
                    char_limit=self.name_char_limit,
                )
                if name in table:
                    out.invalid_name_message()
                    continue
            except user.ConstructionCompleted:
                if len(shooters) < player_min:
                    print("Table must contain at least one player.")
                    continue
                return table, shooters
            prompt_b = f"\n\tEnter a starting bankroll for {name}: "
            bankroll = user.player_bankroll(
                prompt=prompt_b,
                bank_min=self.bank_min,
                bank_max=self.bank_max,
            )
            table[name] = bankroll
            shooters.append(name)
        return table, shooters
        
    def run_sim(self) -> None:
        """Run the main simulation loop.
        
        Track the status of the game and facilitate the cycling between
        game phases. Detect Quit exceptions and handle simulation-ending
        tasks."""

        try:
            while self.game_active:
                if self.puck_on:
                    self.point_cycle()
                else:
                    self.come_out_cycle()
        except user.QuitSim:
            self.log.update_log(
                shooter=self.shooter,
                balance=self.table[self.shooter],
            )
            self.game_active = False
            out.game_log_message(log=self.log.game_log)

    def come_out_cycle(self) -> None:
        """Handle the come out phase of the simulation.
        
        Prompts the user for a pass line bet. Resolves roll results by 
        awarding automatic winners and losers. Exits upon the 
        establishment of a point via the switching of the self.puck_on 
        flag."""
        
        while not self.puck_on and self.game_active:
            pass_line_bet = user.pass_line_prompt(
                shooter=self.shooter,
                bet_min=self.pass_line_min,
                bet_max=self.pass_line_max,
            )        
            if verify.verify_bet_coverage(
                bet=pass_line_bet,
                balance=self.table[self.shooter],
            ):
                self.pass_line_bet = pass_line_bet
            else:
                out.insufficient_balance_message(
                    balance=self.table[self.shooter]
                )
                continue
            total = self._get_come_out_total()
            if total in self.auto_winners:
                out.automatic_winner_message(
                    dice_total=total,
                    bet=self.pass_line_bet
                )
                self.table[self.shooter] = bet.pass_line_win(
                    bet=self.pass_line_bet,
                    balance=self.table[self.shooter],
                )
                out.updated_balance_message(
                    balance=self.table[self.shooter],
                )
            elif total in self.auto_losers:
                out.automatic_loser_message(
                    dice_total=total,
                    bet=self.pass_line_bet,
                )
                self.table[self.shooter] = bet.pass_line_loss(
                    bet=self.pass_line_bet,
                    balance=self.table[self.shooter],
                )
                out.updated_balance_message(
                    balance=self.table[self.shooter],
                )
                if not verify.verify_minimum_balance(
                    balance=self.table[self.shooter],
                    bet_min=self.pass_line_min,
                ):
                    self._find_eligible_shooter()
            else:
                self.point = total
                self.puck_on = True

    def point_cycle(self) -> None:
        """Handle the point cycle phase of the simulation.
        
        Prompts for continued rolls until an exit condition is met.
        Exit conditions are: 
        1) rolling the point total and flipping game phases
        2) a seven out that then rotates shooters or ends the game if no
        shooter is found."""
        
        while self.puck_on and self.game_active:
            total = self._get_point_cycle_total()
            if total == 7:
                out.seven_out_message(bet=self.pass_line_bet)
                self.table[self.shooter] = bet.pass_line_loss(
                    bet=self.pass_line_bet,
                    balance=self.table[self.shooter],
                )
                self.log.update_log(
                    shooter=self.shooter,
                    balance=self.table[self.shooter],
                )
                self._find_eligible_shooter()
                self.log.reset_rolls()
                self.log.reset_points_hit()
                self.point = 0
                self.puck_on = False
            elif total == self.point:
                out.point_hit_message(
                    dice_total=total,
                    bet=self.pass_line_bet,
                )
                self.table[self.shooter] = bet.pass_line_win(
                    bet=self.pass_line_bet,
                    balance=self.table[self.shooter],
                )
                self.log.inc_points()
                self.point = 0
                self.puck_on = False
            else:
                out.trivial_total_message(dice_total=total)

    def _get_come_out_total(self) -> int:
        """Calls the dice roller module function to get a roll result. 
        
        Outputs the roll total message and returns the roll total."""

        user.come_out_prompt(shooter=self.shooter)
        dice1, dice2 = dice.roll_dice()
        total = dice1 + dice2
        self.log.inc_roll()
        out.roll_total_message(dice1=dice1, dice2=dice2)
        return total

    def _get_point_cycle_total(self) -> int:
        """Call the dice roller module function to get a roll result. 
        
        Outputs the roll total message and returns the roll total."""

        user.roll_again_prompt(point=self.point)
        dice1, dice2 = dice.roll_dice()
        total = dice1 + dice2
        self.log.inc_roll()
        out.roll_total_message(dice1=dice1, dice2=dice2)
        return total

    def _find_eligible_shooter(self) -> None:
        """Reference balances and shooters for eligibility.

        Checks shooter balances sequentially until a shooter with a 
        balance above the bet minimum is found. Updates the shooter flag
        to reflect the newly found shooter. Ends the simulation if no
        eligible shooter is found."""

        anchor_index = self.shooters.index(self.shooter)
        candidate_index = verify.inc_shooter_index(
            index=anchor_index,
            shooters=self.shooters,                    
        )
        loop_try_counter = 0
        while loop_try_counter < len(self.shooters):
            next_potential_shooter = self.shooters[candidate_index]
            if verify.verify_minimum_balance(
                balance=self.table[next_potential_shooter],
                bet_min=self.pass_line_min,
            ):
                self.shooter = next_potential_shooter
                break
            else:
                out.skip_shooter_message(shooter=next_potential_shooter)
                candidate_index = verify.inc_shooter_index(
                    index=candidate_index,
                    shooters=self.shooters,
                )
            loop_try_counter += 1
        if loop_try_counter == len(self.shooters):
            out.end_game_message()
            out.game_log_message(log=self.log.game_log)
            self.puck_on = False
            self.game_active = False

def main() -> None:
    try:
        c = Craps()
        c.run_sim()
    except user.QuitSim:
        print("Simulation initialization terminated.")

if __name__ == "__main__":
    main()