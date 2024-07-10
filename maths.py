import numpy as np


def equation_of_line(a, b):
    """
    Determine the equation of the line passing through two points.

    :arg a: the first point the line passes through
    :arg b: the second point the line passes through
    :return: function of two variables defining the line
    """
    if np.allclose(a, b):
        raise ValueError("Cannot determine a unique line through {a} and {b}.")
    x0, y0 = a
    x1, y1 = b

    def f(x, y):
        return (x1 - x0) * (y - y0) - (y1 - y0) * (x - x0)

    return f
