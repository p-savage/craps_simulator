import pytest

import balance_verification


@pytest.mark.parametrize(
    "balance, bet_min, expected_return",
    [(10, 15, False), (15, 15, True), (20, 15, True)]
)
def test_verify_minimum_balance(balance, bet_min, expected_return):

    assert balance_verification.verify_minimum_balance(
        balance, bet_min,
    ) == expected_return

shooters = ['me', 'you', 'him', 'her']
shooter = ['me']
@pytest.mark.parametrize(
    "index, shooters, expected_return",
    [(1, shooters, 2), (3, shooters, 0), (0, shooter, 0)],
)
def test_inc_shooter_index(index, shooters, expected_return):

    assert balance_verification.inc_shooter_index(
        index,
        shooters,
    ) == expected_return

@pytest.mark.parametrize(
    "bet, balance, expected_return",
    [(50, 100, True), (100, 100, True), (100, 99, False)]
)
def test_verify_bet_coverage(bet, balance, expected_return):

    assert balance_verification.verify_bet_coverage(
        bet,
        balance,
    ) == expected_return