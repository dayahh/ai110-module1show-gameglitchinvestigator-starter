from logic_utils import check_guess
from app import parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for the out-of-range bug ---
# Bug: the game accepted 0 (and other out-of-range values) even though it
# claimed the valid range was 1 to 100. parse_guess must reject anything
# outside [low, high].

def test_zero_is_rejected_when_range_starts_at_one():
    # The exact reported bug: 0 was accepted despite a 1-100 range.
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."


def test_out_of_range_guesses_are_rejected():
    out_of_range = [
        ("0", 1, 100),    # below range
        ("101", 1, 100),  # above range
        ("-5", 1, 100),   # negative
        ("21", 1, 20),    # just past the Easy range
        ("51", 1, 50),    # just past the Hard range
    ]
    for raw, low, high in out_of_range:
        ok, value, err = parse_guess(raw, low, high)
        assert ok is False, f"{raw} should be rejected for range {low}-{high}"
        assert value is None
        assert err is not None


def test_in_range_guesses_are_accepted():
    in_range = [
        ("1", 1, 100, 1),      # lower bound is inclusive
        ("100", 1, 100, 100),  # upper bound is inclusive
        ("50", 1, 100, 50),    # mid range
    ]
    for raw, low, high, expected in in_range:
        ok, value, err = parse_guess(raw, low, high)
        assert ok is True, f"{raw} should be accepted for range {low}-{high}"
        assert value == expected
        assert err is None
