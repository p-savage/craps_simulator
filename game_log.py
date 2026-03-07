class GameLog:
    """Class to handle the counters and game log.
    
    Increments points and roll totals. Maintains the game log for the
    simulation session."""

    def __init__(self) -> None:
        """Initialize game log, rolls, and points hit values."""
        
        self.rolls: int = 0
        self.points_hit: int = 0
        self.game_log: list[str] = []

    def inc_roll(self) -> None:
        """Increment the roll counter by 1."""
        
        self.rolls += 1

    def inc_points(self) -> None:
        """Increment the points hit counter by 1."""
        
        self.points_hit += 1

    def reset_points_hit(self) -> None:
        """Reset the points hit counter to 0."""
        
        self.points_hit = 0

    def reset_rolls(self) -> None:
        """Reset the roll counter to 0."""
        
        self.rolls = 0

    def update_log(
        self, 
        shooter: str, 
        balance: int
    ) -> None:
        """Use shooter and balance info to format a new log entry.
        
        Appends logging information to the game log regarding the 
        shooter's roll count, number of points hit, and balance."""

        self.game_log.append(
            f"{shooter} | {self.rolls} Rolls | "
            f"{self.points_hit} Points Hit | Balance ${balance}"
        )