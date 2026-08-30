class QuitSim(Exception):
    """Raised when the user input indicates a Quit request."""

class ConstructionCompleted(Exception):
    """Raised when the user is finished adding players to the table before 
    the maximum player limit is reached."""
    
def player_name(
        prompt: str,
        char_limit: int,
    ) -> str:
    """Use the prompt to get a name entry from the user.
    
    Enforces constraints on character types and string length. Returns 
    the string the user entered stripped of leading or trailing whitespace
    unless custom exception checks are detected."""
    
    while True:
        raw_name = input(prompt)
        name = raw_name.strip().lower()
        if name == "q":
            raise QuitSim()
        if name == "f":
            raise ConstructionCompleted()
        if len(name) > char_limit:
            print("Invalid entry. Maximum of 20 characters.")
            continue
        if not name.isalpha():
            print(
                "Invalid entry. Name must consist of only"
                " alphabetical characters with no spaces."
            )
            continue
        break 
    return raw_name.strip()

def player_bankroll(
        prompt: str,
        bank_min: int,
        bank_max: int,
    ) -> int:
    """Use the prompt to get a bankroll amount from the user.
    
    Enforces integer input requirement from the user. Ensures an 
    acceptable range of possible integers. Returns the starting bankroll
    unless a custom exception check is detected."""

    while True:
        bankroll = input(prompt)
        if bankroll.strip().lower() == "q":
            raise QuitSim()
        try:
            bankroll = int(bankroll)
        except ValueError:
            print(
                "\nBankroll amount must be a numeric value with" 
                " no punctuation or symbols."
            )
            continue
        if bankroll < bank_min or bankroll > bank_max:
            print(
                "\nInvalid entry. Starting bankroll must be in range "
                f"{bank_min} - {bank_max}."
            )
            continue
        break
    return bankroll

def pass_line_prompt(
        shooter: str,
        bet_min: int,
        bet_max: int
    ) -> int:
    """Prompt the shooter for a valid pass line bet amount. 
    
    Enforces integer type and bet min/max constraints. Returns the valid 
    bet unless a custom exception check is detected."""
    
    prompt = (
        f'\n\t{shooter}, place a Pass line wager.\n\tMin: $15, '
        'Max: $100 -> '
    )
    while True:
        response = input(prompt).strip()
        if response.lower() == "q":
            raise QuitSim()
        try:
            pass_line_bet = int(response)
            if pass_line_bet < bet_min:
                print(f"\nMinimum wager amount is ${bet_min}.")
            elif pass_line_bet > bet_max:
                print(f"\nMaximum wager amount is ${bet_max}.")
            else:
                return pass_line_bet
        except ValueError:
            print(
                "\nPlease enter a numeric, whole number bet without the "
                "$"
            )

def come_out_prompt(shooter: str) -> bool:
    """Prompt the shooter for the come out roll.
    
    Returns True upon an Enter key press unless a custom exception check
    is detected."""
    
    prompt = (
        f"\n\t{shooter}, the puck is off. Roll to establish a point.\n"
        "\t(Press Enter to roll or Q to quit)"
    )
    key_press = input(prompt)
    if key_press.strip().lower() == "q":
        raise QuitSim()
    else:
        key_press = True
    return key_press

def roll_again_prompt(point: int) -> bool:
    """State the point and prompt the shooter to continue rolling.
    
    Returns True upon an Enter key press unless a custom exception check
    is detected."""
    
    prompt = (
        f"\n\tThe point is {point}. Hit the point again before "
        "rolling a 7.\n\t(Press Enter to roll or Q to quit)"
    )
    key_press = input(prompt)
    if key_press.strip().lower() == "q":
        raise QuitSim()
    else:
        key_press = True
    return key_press