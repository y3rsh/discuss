import pytest
import max_repeating_chars
from typing import Tuple

LONG_SAME_CHAR = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"


@pytest.mark.unit
@pytest.mark.parametrize(
    "input, input_valid, max_repeat_chars",
    [
        ("josh", True, 1),
        ("qqqqqqqqqq", True, 10),
        ("qqqppp", True, 3),
        ("", False, 0),
        (" ", True, 1),
        (None, False, 0),
        ("✨✨✨😊😊😊😊", True, 4),
        ("**   ()^^$$@@#$", True, 3),
        (LONG_SAME_CHAR, True, 527),
    ],
)
def test_max(input, input_valid, max_repeat_chars):
    outcome: Tuple[bool, int] = max_repeating_chars.max_repeating_chars(input)
    assert outcome[0] == input_valid
    assert outcome[1] == max_repeat_chars
