# Craps Table Simulator

## Overview

This project is a CLI simulator written in Python. It models the
fundamental actions and phases of a craps table. It simulates the table 
and game flow with player names, bankrolls, pass line wagers, dice rolls,
roll outcome resolution, and data logging to track the history of the 
simulation run. The focus of the project was to build a modular 
state-machine. The simulator is composed of a central controlling class 
that coordinates modular components.
Current scope limits the functionality to switching between the come-out
and point phases of the game. There is only one possible bet type - 
the pass line wager. Transition from CLI to GUI or addition of other bet
types are bases for future iterations.

## Features

- Dice roll simulation
- Come-out and point phase switching
- Wager resolution based on roll results
- Rotation through eligible shooters
- State tracking for bankrolls, points, and game stats
- Table construction via user input
- Interactive command line prompts
- Formatted output messages
- User input validation and constraints
- Custom exceptions and exception handling
- Data logging

## Installation

Requires Python version 3.10 or later.
Project written entirely in the standard Python library. No external 
dependencies.

1. Clone the repository and navigate to its directory:

```bash
git clone https://github.com/p-savage/craps_simulator.git
cd craps_simulator
```
2. Run the simulator:

```bash
$ python3 craps.py
```

## Usage and Example Output

The first stage of the simulation involves the construction of the craps
table. Prompts appear in the terminal. There is a maximum number of 
players allowed in any session. Enter `F` to complete table 
construction early and move to the come-out phase.
```text
Welcome to the craps table. Who are our players?

        Enter player name or enter 'F' to finish: Bob

        Enter a starting bankroll for Bob: 75 

        Enter player name or enter 'F' to finish: Alice

        Enter a starting bankroll for Alice: 100

        Enter player name or enter 'F' to finish: f

        Bob, place a Pass line wager.
        Min: $15, Max: $100 -> 
```
The come-out phase begins with a pass line bet placed by the shooter. 
Once a bet is placed, a prompt to roll appears and resulting paths are
taken based upon roll total. Press `Enter` to roll.
```text
        Bob, place a Pass line wager.
        Min: $15, Max: $100 -> 20  

        Bob, the puck is off. Roll to establish a point.
        (Press Enter to roll or Q to quit)

You rolled 3, 4
Winner! 7 is an automatic win. Pass line pays 20.
Bankroll: 95

        Bob, place a Pass line wager.
        Min: $15, Max: $100 -> 50

        Bob, the puck is off. Roll to establish a point.
        (Press Enter to roll or Q to quit)

You rolled 1, 4

        The point is 5. Hit the point again before rolling a 7.
        (Press Enter to roll or Q to quit)
```
In this instance, an automatic winner was achieved and the bet was paid 
out. The next roll established a point for the shooter and the simulation 
moves to the point cycle. The point cycle consists of rolling until
either the point or a 7 is rolled.
```text
        The point is 5. Hit the point again before rolling a 7.
        (Press Enter to roll or Q to quit)    

You rolled 1, 1
2 is not the point.

        The point is 5. Hit the point again before rolling a 7.
        (Press Enter to roll or Q to quit)

You rolled 3, 5
8 is not the point.

        The point is 5. Hit the point again before rolling a 7.
        (Press Enter to roll or Q to quit)

You rolled 2, 5
7 out! Pass line bet loses 50. New shooter.

        Alice, place a Pass line wager.
        Min: $15, Max: $100 -> 
```
At any point, entering `Q` will terminate the simulation session and 
print the session log.
```text
        Alice, place a Pass line wager.
        Min: $15, Max: $100 -> q   


Bob | 5 Rolls | 0 Points Hit | Balance $45
Alice | 0 Rolls | 0 Points Hit | Balance $100

```

## Game Model

The game model follows a common rule set at craps tables. The table 
consists of players. Each player has a bankroll. To be considered for the
shooter role, a player must place a pass line bet. That initiates the 
come-out phase in which the shooter rolls to establish a point. During 
the come-out phase, some roll totals constitute automatic wins and losses
for their pass line bet. This resolves the original bet and a new bet 
must be placed for the come-out to continue. A roll total that is not an
automatic winner or loser is established as the "point".\
Establishing a point begins the point phase of the game. If the shooter 
rolls the point total before rolling a seven, the pass line bet wins. The
shooter retains their shooting privileges and a new come-out phase must 
commence to establish another point. If a seven is rolled before the 
point is hit, it is considered a seven-out. The pass line bet loses. A 
new shooter is found and a new come-out phase is commenced.\
If at any point a loss of a bet drops a player below the pass line 
minimum, they cannot continue as the shooter. Their session statistics 
are still recorded in the game log. But they will be skipped in future
searches for a shooter.  

## Module Structure and Architecture Overview

```
craps.py                ->  main simulation controller and coordinator
config_constants.py     ->  configuration value container
user_input.py           ->  user input prompter and validator
balance_verification.py ->  shooter balance verifier 
bet_outcomes.py         ->  shooter balance updater
output.py               ->  formatted message container
game_log.py             ->  session statistic logger
dice_roller.py          ->  dice roll simulator
```

The central Craps class in craps.py contains the initialization of 
configuration values, constructs the table, handles game state to 
facilitate phase switching, and detects session termination exceptions. 
It calls bet_outcomes.py and balance_verification.py modules for game 
logic needs. Dice_roller.py and game_log.py are simulation infrastructure
modules. User_input.py and output.py handle interactions at the command 
line. Config_constants.py is a container for rule set values.

## Future Improvements

Possible future extensions include:
- Transition from CLI to GUI for visible table state
- Additional bet types with their respective minimums and payout odds:
    - Don't pass
    - Field
    - Hards
    - Buying points
- Real-time display of session roll total distribution
- Pre-configured templates for known betting strategies
- Monte Carlo simulation mode to test betting strategies

## License

This project is licensed under the MIT License. See the LICENSE file for
details.