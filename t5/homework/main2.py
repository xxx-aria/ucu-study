"""Complete all of the following functions. Currently, they all just
'pass' rather than explicitly return value, meaning they
implicitly return None. They all include doctests, which you can
test by running this file.
The doctests are just examples. Feel free to add your own doctests."""


# ****************************************
# Problem 1
# ****************************************
def lines_intersection(
    k1: int | float, c1: int | float, k2: int | float, c2: int | float
) -> tuple | None:
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

    >>> lines_intersection('2', -2, 1, 0)

    >>> lines_intersection('a', 'b', 'c', 'd')

    >>> lines_intersection(3, 4, 3, 7)

    >>> lines_intersection(207, -324, 137, 91)
    (5.929, 903.214)
    >>> lines_intersection(1, 0, 2, 0)
    (0.0, 0.0)
    >>> lines_intersection(241789, 1245512, 8824156, 984294)
    (0.03, 1252871.233)
    >>> lines_intersection(123456, 100, 2, 200)
    (0.001, 200.002)
    >>> lines_intersection(123456, 1, 0, 2)
    (0.0, 2.0)
    """

    if not (
        type(k1) in (int, float)
        and type(c1) in (int, float)
        and type(k2) in (int, float)
        and type(c2) in (int, float)
    ):
        return None

    if k1 == k2:
        return None

    point_x = (c2 - c1) / (k1 - k2)
    point_y = k1 * point_x + c1

    # + 0.0 normalizes -0.0
    return (round(point_x, 3) + 0.0, round(point_y, 3) + 0.0)


# ****************************************
# Problem 2
# ****************************************
def distance(x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> float | None:
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
    >>> distance(0, 0, 0, 0)
    0.0
    >>> distance('a', 1, -1, 1)

    >>> distance(1234567, 999999, 2234, 34)
    1587001.772
    >>> distance(1234567, 111111, 1234568, 1111112)
    1000001.0
    >>> distance(1.0001, 1.0002, 1.0003, 1.0004)
    0.0
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(0, 0, -3, -4)
    5.0
    >>> distance(0, 0, 99999999, 0)
    99999999.0
    """

    if not (
        type(x1) in (int, float)
        and type(y1) in (int, float)
        and type(x2) in (int, float)
        and type(y2) in (int, float)
    ):
        return None

    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 3)


# ****************************************
# Problem 3
# ****************************************
def quadrangle_area(
    a: int | float, b: int | float, c: int | float, d: int | float, f1: int | float, f2: int | float
) -> float | None:
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

    >>> quadrangle_area(3, 4, '3', 4, '5', 5)

    >>> quadrangle_area(3, -4, 3, 3, 1, -1)

    >>> quadrangle_area(31343, 14133, 34431, 731455, 9215215, 1712784)
    7890711145784.954
    >>> quadrangle_area(7, 2, 10, 0, 12, 15)

    >>> quadrangle_area(0.007, 0.02, 0.01, 0.005, 1.2, 0.15)
    0.09
    >>> quadrangle_area(0.0007, 0.002, 0.001, 0.0005, 0.12, 0.015)
    0.001
    >>> quadrangle_area(0.0001, 0.002, 0.0003, 0.004, 0.005, 0.006)
    0.0
    >>> quadrangle_area(2, 2, 2, 2, 2.8284271247461903, 2.8284271247461903)
    4.0
    >>> quadrangle_area(2, 2, 2, 2, 2, 2)
    2.0
    """
    if not (
        type(a) in (int, float)
        and type(b) in (int, float)
        and type(c) in (int, float)
        and type(d) in (int, float)
        and type(f1) in (int, float)
        and type(f2) in (int, float)
    ):
        return None

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return None
    if f1 <= 0 or f2 <= 0:
        return None

    area_squared = (4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2) ** 2) / 16
    if area_squared < 0:
        return None

    return round(area_squared**0.5, 3)


# ****************************************
# Problem 4
# ****************************************
def four_lines_area(
    k1: int | float,
    c1: int | float,
    k2: int | float,
    c2: int | float,
    k3: int | float,
    c3: int | float,
    k4: int | float,
    c4: int | float,
) -> float | int | None:
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
    >>> four_lines_area(0, 20, 'a', -0.3, 0.1, 'b', -5, 3)

    >>> four_lines_area(0, 0, 0, 0, 0, 0.0, 0, 0.0)
    0
    >>> four_lines_area(2, 2, -2, 2, 2, -2, -2, -2)
    4.0
    >>> four_lines_area(5, 0, -1, 0, 7, 0, -2, 0)
    0
    """

    if not (
        type(k1) in (int, float)
        and type(c1) in (int, float)
        and type(k2) in (int, float)
        and type(c2) in (int, float)
        and type(k3) in (int, float)
        and type(c3) in (int, float)
        and type(k4) in (int, float)
        and type(c4) in (int, float)
    ):
        return None

    vertex_1 = lines_intersection(k1, c1, k2, c2)
    vertex_2 = lines_intersection(k2, c2, k3, c3)
    vertex_3 = lines_intersection(k3, c3, k4, c4)
    vertex_4 = lines_intersection(k4, c4, k1, c1)

    # check whether adjacent lines are parallel
    if not (vertex_1 and vertex_2 and vertex_3 and vertex_4):
        return 0

    # check whether vertices are not the same points
    if (
        vertex_1 in (vertex_2, vertex_3, vertex_4)
        or vertex_2 in (vertex_3, vertex_4)
        or vertex_3 == vertex_4
    ):
        return 0

    vertex_1_x, vertex_1_y = vertex_1
    vertex_2_x, vertex_2_y = vertex_2
    vertex_3_x, vertex_3_y = vertex_3
    vertex_4_x, vertex_4_y = vertex_4

    side_1 = distance(vertex_1_x, vertex_1_y, vertex_2_x, vertex_2_y)
    side_2 = distance(vertex_2_x, vertex_2_y, vertex_3_x, vertex_3_y)
    side_3 = distance(vertex_3_x, vertex_3_y, vertex_4_x, vertex_4_y)
    side_4 = distance(vertex_4_x, vertex_4_y, vertex_1_x, vertex_1_y)
    diagonal_1 = distance(vertex_1_x, vertex_1_y, vertex_3_x, vertex_3_y)
    diagonal_2 = distance(vertex_2_x, vertex_2_y, vertex_4_x, vertex_4_y)

    area = quadrangle_area(side_1, side_2, side_3, side_4, diagonal_1, diagonal_2)
    if not area:
        return 0

    return area


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
