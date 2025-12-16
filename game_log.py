class GameLog:
    """Handle the counters and game log"""

    def __init__(self):
        """Initialize game log values"""
        self.shooter = 1
        self.rolls = 0
        self.points_hit = 0
        self.game_log = []

    def inc_shooter(self):
        """Increment the shooter counter"""
        self.shooter += 1

    def inc_roll(self):
        """Increment the roll counter"""
        self.rolls += 1

    def inc_points(self):
        """Increment the points hit counter"""
        self.points_hit += 1

    def reset_points_hit(self):
        """Reset the points hit counter"""
        self.points_hit = 0

    def reset_rolls(self):
        """Reset the roll counter"""
        self.rolls = 0

    def update_log(self, balance):
        self.game_log.append(
        f'Shooter {self.shooter} : {self.rolls} Rolls : '+
        f'{self.points_hit} Points Hit : Balance ${balance}'
        )