import collections
from typing import Tuple


def max_repeating_chars(input: str) -> Tuple[bool, int]:
    """
    Return the max number of repeating characters in a string
    and a boolean describing the validity of the passed string.
    Do not trust the passed parameter and exit fast with false
    validity and length 0 upon non-string or empty parameter.
    """
    # empty strings are "falsy" in python
    if not input:
        return (False, 0)
    input_length = len(input)

    if input_length == 1 or (len(set(input)) == input_length):
        return (True, 1)

    max_reapeat = collections.Counter(input).most_common(1)[0][1]
    return (True, max_reapeat)
