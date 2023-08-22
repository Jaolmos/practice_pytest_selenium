import pytest


def add_two_numbers(num1, num2):
    return num1 + num2

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(2, 3) == 5, "The sum of 2 and 3 should be 5"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(200, 300) == 500, "The sum of 200 and 300 should be 500"