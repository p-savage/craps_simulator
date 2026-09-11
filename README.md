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
dependencies to operate the simulator.

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

The central Craps class in `craps.py` initializes configuration values,
constructs the table, handles game state to facilitate phase switching,
and detects session termination exceptions. It calls `bet_outcomes.py`
and `balance_verification.py` modules to handle game logic.
`dice_roller.py` and `game_log.py` are simulation infrastructure modules.
`user_input.py` and `output.py` handle interactions at the command line. `config_constants.py` is a container for rule set values.

## Testing

While the operation of the simulator requires no external dependencies,
an optional unit-test suite is included. It will require some very light
setup before utilization.\
A virtual environment is recommended to keep project dependencies
contained. A virtual environment can be created easily from the command
line. Navigate to the project's root directory and run:
```text
python3 -m venv venv
```
This will create a new folder in the project directory called `venv`. Now
the virtual environment needs to be activated. That can be done by
running:
```text
source venv/bin/activate
```
The command prompt should now start with `(venv)`.\
With an activated virtual environment in the project's directory, pytest
can be installed without affecting the system's global environment. To do
that, run:
```text
pip install pytest
```
With pytest installed, run:
```text
pytest
```
Executing this command from the project root directory with an activated
virtual environment will automatically detect the three modules that
begin with `test_`. The test functions in those modules will be executed
automatically and the default output will look like this:
```text
(venv) (your command prompt) craps % pytest                       
==================== test session starts ====================
platform darwin -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0
rootdir: (full path to your project root directory)
collected 29 items                                                                                                                                                                                                                                                

test_balance_verification.py .........
[ 31%]
test_bet_outcomes.py ..
[ 37%]
test_user_input.py ..................
[100%]

==================== 29 passed in 0.03s ====================
(venv) (your command prompt) craps % 
```
The "Future Improvements" section outlines some possible feature
expansions. Should their implementation be attempted, the unit-tests
will be a useful tool for detecting any changes that break an important
block of logic. For instance, say that some future editing session
changes line 8 of `bet_outcomes.py` from
```
balance += bet
```
to 
```
balance -= bet
```
Now, when the simulator calls `pass_line_win()`, the bet amount will be
deducted from the shooter's balance. This will cause many problems for a
simulator that is built assuming that bet-wins increase a shooter's
balance. Running pytest will report a failure - signaling that some
block of code has been altered in a way that breaks the broader function
of the simulator. The output will look like this:
```text
(venv) (your command prompt) craps % pytest
==================== test session starts ====================
platform darwin -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0
rootdir: (full path to your project root directory)
collected 29 items                                                                      

test_balance_verification.py .........                                            [ 31%]
test_bet_outcomes.py F.                                                           [ 37%]
test_user_input.py ..................                                             [100%]

==================== FAILURES ====================
__________ test_pass_line_win_increases_balance_by_bet __________

    def test_pass_line_win_increases_balance_by_bet():
    
        bet = 15
        balance = 100
>       assert bet_outcomes.pass_line_win(bet=bet, balance=balance) == 115
E       assert 85 == 115
E        +  where 85 = <function pass_line_win at 0x10378a340>(bet=15, balance=100)
E        +    where <function pass_line_win at 0x10378a340> = bet_outcomes.pass_line_win

test_bet_outcomes.py:15: AssertionError
==================== short test summary info ====================
FAILED test_bet_outcomes.py::test_pass_line_win_increases_balance_by_bet - assert 85 == 115
==================== 1 failed, 28 passed in 0.07s ====================
(venv) (your command prompt) craps % 
```
A concise description of the
issue is shown towards the bottom under `short test summary info`.
```text
FAILED test_bet_outcomes.py::test_pass_line_win_increases_balance_by_bet - assert 85 == 115
```
That specifies the test module, function, and assertion that failed so
debugging can be as efficient as possible.

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