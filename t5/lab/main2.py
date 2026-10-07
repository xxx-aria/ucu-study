"""Complete all of the following functions. Currently, they all just
'pass' rather than explicitly return value, meaning they
implicitly return None. They all include doctests, which you can
test by running this file.
The doctests are just examples. Feel free to add your doctests."""


# ****************************************
# Problem 1
# ****************************************
def type_by_angles(alpha, beta, gamma):
    """
    Detect the type of triangle by its angles in degrees and return
    the type as a string ("right triangle", "obtuse triangle", "acute triangle").

    If there is no triangle with such angles, then the function should return None.
    If the arguments are not numbers, the function should return None.

    :param alpha: int, The first angle of the triangle.
    :param beta: int, The second angle of the triangle.
    :param gamma: int, The third angle of the triangle.
    :return: str or None, The type of triangle or None if the angles do not
    form a triangle.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right triangle'
    >>> type_by_angles(120, 30, 30)
    'obtuse triangle'
    >>> type_by_angles(2015, 2015, 2015) is None
    True
    """

    if not isinstance(alpha, int) or not isinstance(beta, int) or not isinstance(gamma, int):
        return

    max_angle = max(alpha, beta, gamma)
    min_angle = min(alpha, beta, gamma)

    if alpha + beta + gamma != 180 or min_angle <= 0:
        return

    if min_angle < 90 and max_angle < 90:
        triangle_type = 'acute triangle'
    elif max_angle == 90:
        triangle_type = 'right triangle'
    else:  # max_angle > 90
        triangle_type = 'obtuse triangle'

    return triangle_type


# ****************************************
# Problem 2
# ****************************************
def type_by_sides(a, b, c):
    """
    Detect the type of triangle by its sides and return the type as a string
    ("right triangle", "obtuse triangle", "acute triangle").

    If there is no triangle with such sides, then the function should return None.
    If the arguments are not numbers, the function should return None.

    :param a: int or float, The first side of the triangle.
    :param b: int or float, The second side of the triangle.
    :param c: int or float, The third side of the triangle.
    :return: str or None, The type of triangle or None if the sides do not
    form a triangle.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right triangle'
    >>> type_by_sides(3, 4, 6)
    'obtuse triangle'
    >>> type_by_sides(3, 3, 2015)
    """

    if (not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int)) and (
        not isinstance(a, float) or not isinstance(b, float) or not isinstance(c, float)
    ):
        return

    max_side = max(a, b, c)
    min_side = min(a, b, c)
    mid_side = (a + b + c) - max_side - min_side

    if min_side <= 0:
        return
    if max_side > min_side + mid_side:
        return

    if max_side**2 == mid_side**2 + min_side**2:
        triangle_type = 'right triangle'
    elif max_side**2 > mid_side**2 + min_side**2:
        triangle_type = 'obtuse triangle'
    else:
        triangle_type = 'acute triangle'

    return triangle_type


# ****************************************
# Problem 3
# ****************************************
def get_letters(n):
    """
    Create and return a string of the first n letters
    of the Latin alphabet (26 letters in total).

    If the argument isn't a positive integer, or greater
    than 26, the function should return None.

    >>> get_letters(0)
    >>> get_letters(1)
    'a'
    >>> get_letters(6)
    'abcdef'
    >>> get_letters(-2015)
    """

    if not isinstance(n, int):
        return
    if n <= 0 or n > 26:
        return

    letters = ''
    for i in range(n):
        letters += chr(ord('a') + i)

    return letters


# ****************************************
# Problem 4
# ****************************************
def number_of_capital_letters(s):
    """
    Find and return number of capital letters in string.

    If the argument isn't a string, the function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters("EOFErr1or")
    4
    >>> number_of_capital_letters(1)
    """
    pass


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
