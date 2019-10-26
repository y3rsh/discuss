import pytest


def fail_fast(expression):
    if not expression or len(expression) % 2 != 0:
        return True
    return False


def is_matched(expression):
    if fail_fast(expression):
        return False
    mapping = {"(": ")", "{": "}", "[": "]"}
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif not (queue and letter == queue.pop()):
            return False
    return not queue


@pytest.mark.unit
@pytest.mark.parametrize(
    "input, output",
    [
        ("]{}", False),
        ("{(})", False),
        ("{()}", True),
        ("[({({{{}}})})]", True),
        (None, False),
        ("", False),
    ],
)
def test_matching_braces(input, output):
    assert is_matched(input) == output


mapping = dict(zip("({[", ")}]"))
mapping = {"(": ")", "{": "}", "[": "]"}
