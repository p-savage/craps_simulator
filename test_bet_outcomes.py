"""
Tests for the bet_outcomes module:

Balance addition on a win and subtraction on a loss.
"""


import bet_outcomes


def test_pass_line_win_increases_balance_by_bet():

    bet = 15
    balance = 100
    assert bet_outcomes.pass_line_win(bet=bet, balance=balance) == 115


def test_pass_line_loss_decreases_balance_by_bet():

    bet = 15
    balance = 100
    assert bet_outcomes.pass_line_loss(bet=bet, balance=balance,) == 85
