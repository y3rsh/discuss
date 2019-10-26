import pytest
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(min_value=-1, max_value=3))
def test_compute(param1):
    print(f"{param1 = }") # 3.8 😉
    assert param1 < 4