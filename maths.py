from sympy import Line, Point2D
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
    line = Line(Point2D(a), Point2D(b))

    def evaluate(x, y):
        return float(line.distance(Point2D((x, y))))

    return evaluate
