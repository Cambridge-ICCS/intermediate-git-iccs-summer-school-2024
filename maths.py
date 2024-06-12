def equation_of_line(a, b):
    """
    Determine the equation of the line passing through two points.

    :arg a: the first point the line passes through
    :arg b: the second point the line passes through
    :return: function of two variables defining the line
    """
    x0, y0 = a
    x1, y1 = b

    if (x0 == x1):
        # Special case of a vertical line

        def f(x, y):
            return x - x0

    else:

        def f(x, y):
            m = (y1 - y0) / (x1 - x0)
            c = y0 - m * x0
            return y - m * x - c

    return f
