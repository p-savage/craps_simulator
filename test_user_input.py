"""
Tests for the user_input module:

Custom exception behavior, appropriate char types, char number limits,
min and max values for numeric inputs, disregard for leading chars when
only Enter presses are required.
"""


import pytest

import user_input
from config_constants import (
    BANKROLL_MAX,
    BANKROLL_MIN,
    CHAR_LIMIT,
    PASS_LINE_MAX,
    PASS_LINE_MIN,
)


def test_player_name_quit_request(monkeypatch):

    def return_q(text: str):
        return "q"
    monkeypatch.setattr(user_input, "input", return_q, raising=False)
    with pytest.raises(user_input.QuitSim):
        user_input.player_name("prompt", 2)


def test_player_name_completed_construction_request(monkeypatch):

    def return_f(text: str):
        return "f"
    monkeypatch.setattr(user_input, "input", return_f, raising=False)
    with pytest.raises(user_input.ConstructionCompleted):
        user_input.player_name("prompt", 2)


char_limit_input_sequence = [('w'*(CHAR_LIMIT+1)), ('w'*CHAR_LIMIT)]
def test_player_name_char_limit(monkeypatch):

    iterator = iter(char_limit_input_sequence)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.player_name(
        "prompt",
        char_limit=CHAR_LIMIT,
    ) == ('w'*CHAR_LIMIT)


alpha_char_input_sequence = ['3', '!', 'c a', '}', 'C  ']
def test_player_name_alpha_chars(monkeypatch):
    """
    Tests input sequences for handling of different char types.

    Non-alphabetical chars should be rejected. Trailing whitespace is
    acceptable but internal whitespace is rejected. Capitalization for
    permissible input should be preserved. 
    """

    iterator = iter(alpha_char_input_sequence)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.player_name("prompt", char_limit=CHAR_LIMIT) == 'C'


def test_player_bankroll_quit_request(monkeypatch):

    def return_q(text: str):
        return "q"
    monkeypatch.setattr(user_input, "input", return_q, raising=False)
    with pytest.raises(user_input.QuitSim):
        user_input.player_bankroll("prompt", BANKROLL_MIN, BANKROLL_MAX)


bankroll_value_error_input_sequence = [
    'one hundred',
    '$100',
    '100.00',
    str(BANKROLL_MIN+1),
]
def test_bankroll_value_error_branch(monkeypatch):

    iterator = iter(bankroll_value_error_input_sequence)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.player_bankroll(
        "prompt",
        bank_min=BANKROLL_MIN,
        bank_max=BANKROLL_MAX,
    ) == (BANKROLL_MIN+1)


bankroll_low_input_sequence = [str(BANKROLL_MIN - 5), str(BANKROLL_MIN)]
bankroll_high_input_sequence = [str(BANKROLL_MAX + 5), str(BANKROLL_MAX)]
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (bankroll_low_input_sequence, BANKROLL_MIN),
        (bankroll_high_input_sequence, BANKROLL_MAX)
    ],
)
def test_bankroll_min_max_branch(
    monkeypatch,
    input_list,
    expected_output,
):

    iterator = iter(input_list)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.player_bankroll(
        "prompt",
        bank_min=BANKROLL_MIN,
        bank_max=BANKROLL_MAX,
    ) == expected_output


def test_pass_line_prompt_quit_request(monkeypatch):

    def return_q(text: str):
        return "q"
    monkeypatch.setattr(user_input, "input", return_q, raising=False)
    with pytest.raises(user_input.QuitSim):
        user_input.pass_line_prompt(
            "shooter",
            bet_min=PASS_LINE_MIN,
            bet_max=PASS_LINE_MAX,
        )


pass_line_value_error_input_sequence = [
    'one hundred',
    '$100',
    '100.00',
    str(PASS_LINE_MIN+1),
]
def test_pass_line_value_error_branch(monkeypatch):

    iterator = iter(pass_line_value_error_input_sequence)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.pass_line_prompt(
        "shooter",
        bet_min=PASS_LINE_MIN,
        bet_max=PASS_LINE_MAX,
    ) == (PASS_LINE_MIN+1)


pass_line_low_inputs = [str(PASS_LINE_MIN-5), str(PASS_LINE_MIN)]
pass_line_high_inputs = [str(PASS_LINE_MAX+5), str(PASS_LINE_MAX)]
@pytest.mark.parametrize(
    "input_list, expected_outcome",
    [
        (pass_line_low_inputs, PASS_LINE_MIN),
        (pass_line_high_inputs, PASS_LINE_MAX),
    ],
)
def test_pass_line_min_max_branch(
    monkeypatch,
    input_list,
    expected_outcome,
):

    iterator = iter(input_list)
    def next_input(text: str):
        return next(iterator)
    monkeypatch.setattr(user_input, "input", next_input, raising=False)
    assert user_input.pass_line_prompt(
        "shooter",
        bet_min=PASS_LINE_MIN,
        bet_max=PASS_LINE_MAX,
    ) == expected_outcome


def test_come_out_prompt_quit_request(monkeypatch):

    def return_q(text: str):
        return "q"
    monkeypatch.setattr(user_input, "input", return_q, raising=False)
    with pytest.raises(user_input.QuitSim):
        user_input.come_out_prompt("shooter")


come_out_first_input = 'lakjlkj5646'
come_out_second_input = ''
@pytest.mark.parametrize(
        "string, expected_output",
        [(come_out_first_input, True), (come_out_second_input, True)]
)
def test_come_out_prompt_input_branch(
    monkeypatch,
    string,
    expected_output,
):

    def return_string(text: str):
        return string
    monkeypatch.setattr(
        user_input,
        "input",
        return_string,
        raising=False,
    )
    assert user_input.come_out_prompt("shooter") == expected_output


def test_roll_again_prompt_quit_request(monkeypatch):

    def return_q(text: str):
        return "q"
    monkeypatch.setattr(user_input, "input", return_q, raising=False)
    with pytest.raises(user_input.QuitSim):
        user_input.roll_again_prompt(point=5)


roll_again_first_input = 'lakjlkj5646'
roll_again_second_input = ''
@pytest.mark.parametrize(
        "string, expected_output",
        [(roll_again_first_input, True), (roll_again_second_input, True)]
)
def test_roll_again_prompt_input_branch(
    monkeypatch,
    string,
    expected_output,
):

    def return_string(text: str):
        return string
    monkeypatch.setattr(
        user_input,
        "input",
        return_string,
        raising=False,
    )
    assert user_input.roll_again_prompt(point=5) == expected_output
