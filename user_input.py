def quit_check(user_input):
    """Check if input is 'q' for quit"""
    if user_input.strip().lower() == 'q':
        return True

def pass_line_prompt(shooter):
    """Prompt the shooter for a valid pass line bet amount"""
    prompt = (f'\n\tShooter {shooter}, place'+
                ' a "Pass" line wager.\n\tMin: $15, Max: $100 -> ')
    while True:
        amount = input(prompt).strip()
        if quit_check(amount):
            return False
        try :
            pass_line_bet = int(amount)
            if pass_line_bet < 15:
                print("\nMinimum wager amount is $15.")
            elif pass_line_bet > 100:
                print("\nMaximum wager amount is $100.")
            else:
                print(pass_line_bet)
                return pass_line_bet
        except ValueError:
            print("\nPlease enter a numeric, "+
                  "whole number bet without the $")
    
    ### mixed data types as possible outputs (int & bool) ###

def come_out_prompt(shooter):
    """Prompt the shooter for the come out roll"""
    prompt = (f"\n\tShooter {shooter}, the puck is off."+
                " Roll to establish a point.\n"+
                "\t(Press Enter to roll or Q to quit)")
    key_press = input(prompt)
    if quit_check(key_press):
        key_press = False
    else:
        key_press = True
    return key_press

def roll_again_prompt(point):
    """State the point and prompt the shooter to continue rolling"""
    prompt = (
            f"\n\tThe point is {point}. Hit the point again before rolling a 7.\n"+
            "\t(Press Enter to roll or Q to quit)"
            )
    key_press = input(prompt)
    if quit_check(key_press):
        key_press = False
    else:
        key_press = True
    return key_press