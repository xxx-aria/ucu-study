"""Complete all of the following functions. Currently, they all just
'pass' rather than explicitly return value, meaning they
implicitly return None. They all include doctests, which you can
test by running this file.
The doctests are just examples. Feel free to add your own doctests."""


# ****************************************
# Problem 1
# ****************************************
def lines_intersection(k1, c1, k2, c2):
    """
    Find the intersection point of two lines.

    Each line is given by the coefficients of its equation y = k*x + c.
    The intersection point is found by solving k1*x + c1 = k2*x + c2.
    The function returns a tuple of two floats (x, y), each coordinate
    rounded to 3 decimal places.

    If the lines are parallel or coincide (k1 == k2), there is no single
    intersection point and the function should return None.

    :param k1: int or float, The slope of the first line.
    :param c1: int or float, The intercept of the first line.
    :param k2: int or float, The slope of the second line.
    :param c2: int or float, The intercept of the second line.
    :return: tuple or None, The intersection point (x, y) rounded to
             3 decimal places, or None if the lines do not intersect
             in a single point.

    >>> lines_intersection(2, -2, 1, 0)
    (2.0, 2.0)
    >>> lines_intersection(3, -0.3, -5, 3)
    (0.412, 0.937)
    >>> lines_intersection(3, 4, 3, -10)

    >>> lines_intersection(2, 7, 2, 7)

    """
    pass


# ****************************************
# Problem 2
# ****************************************
def distance(x1, y1, x2, y2):
    """
    Find the distance between two points.

    The points are given by their coordinates (x1, y1) and (x2, y2).
    The distance is computed by the formula:
    sqrt((x2 - x1)**2 + (y2 - y1)**2)
    The function returns one float: the distance rounded to 3 decimal
    places.

    :param x1: int or float, The x-coordinate of the first point.
    :param y1: int or float, The y-coordinate of the first point.
    :param x2: int or float, The x-coordinate of the second point.
    :param y2: int or float, The y-coordinate of the second point.
    :return: float, The distance between the points rounded to
             3 decimal places.

    >>> distance(1, 1, 6, 3)
    5.385
    >>> distance(-1, 1, 3, 1)
    4.0
    >>> distance(-1, 1, -1, 1)
    0.0
    """
    pass


# ****************************************
# Problem 3
# ****************************************
def quadrangle_area(a, b, c, d, f1, f2):
    """
    Find the area of a quadrangle given its sides and diagonals.

    The quadrangle has consecutive sides of lengths a, b, c, d and
    diagonals of lengths f1 and f2. The area S is computed from the
    relation:
    16 * S**2 = 4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2
    The function returns one float: the area S rounded to 3 decimal
    places.

    If the right-hand side of the relation is negative, a quadrangle
    with such sides and diagonals does not exist and the function
    should return None.

    :param a: int or float, The first side of the quadrangle.
    :param b: int or float, The second side of the quadrangle.
    :param c: int or float, The third side of the quadrangle.
    :param d: int or float, The fourth side of the quadrangle.
    :param f1: int or float, The first diagonal of the quadrangle.
    :param f2: int or float, The second diagonal of the quadrangle.
    :return: float or None, The area rounded to 3 decimal places,
             or None if such a quadrangle does not exist.

    >>> quadrangle_area(3, 4, 3, 4, 5, 5)
    12.0
    >>> quadrangle_area(3, 4, 3, 3, 1, 1)

    """
    pass


# ****************************************
# Problem 4
# ****************************************
def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    Find the area of the convex quadrilateral bounded by four lines.

    Each side of the quadrilateral lies on a line y = k*x + c, and the
    four lines are given in adjacent order: line 1 is adjacent to
    lines 2 and 4, line 2 is adjacent to lines 1 and 3, and so on.
    Opposite lines (1 and 3, 2 and 4) may be parallel.

    The four vertices of the quadrilateral are the intersection points
    of the adjacent pairs of lines: lines 1 and 2, lines 2 and 3,
    lines 3 and 4, lines 4 and 1. The sides connect consecutive
    vertices, and the diagonals connect vertex 1 with vertex 3 and
    vertex 2 with vertex 4.

    Use the helper functions: lines_intersection() for the vertices,
    distance() for the lengths of the sides and diagonals, and
    quadrangle_area() for the area. The function returns the area
    rounded to 3 decimal places.

    If such a quadrilateral does not exist (some adjacent lines are
    parallel, e.g. three parallel lines, or the vertices do not form
    a quadrangle), the function should return 0.

    :param k1: int or float, The slope of the first line.
    :param c1: int or float, The intercept of the first line.
    :param k2: int or float, The slope of the second line.
    :param c2: int or float, The intercept of the second line.
    :param k3: int or float, The slope of the third line.
    :param c3: int or float, The intercept of the third line.
    :param k4: int or float, The slope of the fourth line.
    :param c4: int or float, The intercept of the fourth line.
    :return: float or int, The area of the quadrilateral rounded to
             3 decimal places, or 0 if it does not exist.

    >>> four_lines_area(1, 10, -1, 10, 1, -10, -1, -10)
    200.0
    >>> four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3)
    74.49
    >>> four_lines_area(1, 1, 1, 2, 1, 3, 0, 0)
    0
    """
    pass


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
