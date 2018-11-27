import sys

import pytest
from unittest_pytest import mathlib


@pytest.mark.skip(reason="I don't want to run this test now")
@pytest.mark.skipif(sys.version_info > (3, 5))
def test_calc_total():
    result = mathlib.calc_total(4, 5)
    assert result == 9


def test_calc_multiply():
    result = mathlib.calc_multipy(10, 3)
    assert result == 30


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output
