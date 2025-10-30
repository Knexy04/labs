import math
import pytest

from lab6.calculator import Calculator


@pytest.fixture()
def calc() -> Calculator:
    return Calculator()


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ((), 0.0),
        ((0,), 0.0),
        ((1,), 1.0),
        ((1, 2), 3.0),
        ((-5, 2.5), -2.5),
        ((1, 2, 3, 4, 5), 15.0),
    ],
)
def test_add(calc: Calculator, inputs, expected):
    assert calc.add(*inputs) == pytest.approx(expected)


@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (10, 2, 5.0),
        (-9, 3, -3.0),
        (5, 2, 2.5),
        (0, 7, 0.0),
    ],
)
def test_divide_valid(calc: Calculator, numerator, denominator, expected):
    assert calc.divide(numerator, denominator) == pytest.approx(expected)


def test_divide_by_zero_raises(calc: Calculator):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


@pytest.mark.parametrize(
    "value, expected",
    [
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (9, False),
        (11, True),
        (25, False),
        (29, True),
        (97, True),
        (100, False),
    ],
)
def test_is_prime_number(calc: Calculator, value, expected):
    assert calc.is_prime_number(value) is expected
