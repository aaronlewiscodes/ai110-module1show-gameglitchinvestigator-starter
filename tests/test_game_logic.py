from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_go_lower_hint_message():
    # When guess exceeds the secret, the hint message should tell the player to go lower
    outcome, message = check_guess(75, 42)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_go_lower_hint_by_one():
    # Edge case: guess is exactly one above the secret
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_go_lower_not_shown_when_correct():
    # Winning guess should not produce a Go Lower hint
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "LOWER" not in message

def test_go_lower_not_shown_when_too_low():
    # A low guess should not produce a Go Lower hint
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "LOWER" not in message
