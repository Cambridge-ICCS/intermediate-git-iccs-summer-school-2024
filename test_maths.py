from maths import *
import numpy as np
import pytest


@pytest.mark.parametrize(
    "a,b,condition",
    [
        ((0, 0), (0, 1), lambda x, y: x == 0),
        ((0, 0), (1, 0), lambda x, y: y == 0),
        ((0, 0), (1, 1), lambda x, y: x == y),
    ]
)
def test_equation(a, b, condition):
    f = equation_of_line(a, b)
    for (x, y) in [(i, j) for j in range(10) for i in range(10)]:
        iszero = np.isclose(f(x, y), 0)
        if (not iszero if condition(x, y) else iszero):
            raise AssertionError(f"f({x},{y}) {'!=' if condition(x, y) else '=='} 0")
