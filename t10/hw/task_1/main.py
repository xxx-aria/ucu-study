"""
Calculus: maximal values, limits, derivatives, tangents and roots.
"""

from itertools import count


def find_max_value(func: callable, points: list[float]) -> float:
    """Find the maximal value of a function at given points.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        float: The maximal value of the function at the given points
               rounded to 2 decimal places.

    Examples:

    >>> find_max_value(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return round(max(map(func, points)), 2)


def find_max_points(func: callable, points: list[float]) -> set[float]:
    """Find the points where the function has the maximal value.

    Compare the exact (not rounded) values of the function.

    Args:
        func (callable): The function to evaluate.
        points (list[float]): A list of points at which to evaluate the function.

    Returns:
        set[float]: A set of points where the function has the maximal value.

    Examples:
    >>> find_max_points(lambda x: x ** 2 + x, [1, 2, 3, -1])
    {3}
    >>> find_max_points(lambda x: -x ** 2 + 4*x, [1, 0, 3, -1])
    {1, 3}
    """
    max_v = max(map(func, points))
    max_p = set()
    for p, v in map(lambda x: (x, func(x)), points):
        if v == max_v:
            max_p.add(p)
    return max_p


def compute_limit(seq: callable) -> float:
    """Compute the limit of a convergent sequence.

    Args:
        seq (callable): A function representing the sequence.

    Returns:
        float: The limit of the sequence rounded to 2 decimal places.

    Examples:
        >>> compute_limit(lambda n: (n ** 2 + n) / (3*n ** 2))
        0.33
    """
    epsilon = 0.001
    res = None
    for n in map(lambda p: 10**p, count(0, step=1)):
        n_next = n * 10
        if abs(seq(n_next) - seq(n)) < epsilon:
            res = round(seq(n_next), 2)
            break
    return res


def compute_derivative(func: callable, x_0: float) -> float:
    """Compute the derivative of a function at a given point.

    Args:
        func (callable): The function to differentiate.
        x_0 (float): The point at which to compute the derivative.

    Returns:
        float: The derivative of the function at the given point
               rounded to 2 decimal places.

    Examples:
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    epsilon = 0.001
    res = None
    for dx in map(lambda p: 10 ** (-p), count(0, step=1)):
        dx_next = dx / 10
        lim_dx = (func(x_0 + dx) - func(x_0)) / dx
        lim_dx_next = (func(x_0 + dx_next) - func(x_0)) / dx_next
        if abs(lim_dx - lim_dx_next) < epsilon:
            res = round(lim_dx_next, 2)
            break
    return res


def get_tangent(func: callable, x_0: float) -> str:
    """Calculate the equation of the tangent line to a given function at a specified point.

    This function computes the tangent line to the input function `func` at the point `x_0`.
    The tangent line is represented in the form of a linear equation.

    Args:
        func (callable): A function for which the tangent line is to be calculated.
        x_0 (float): The x-coordinate at which the tangent line is computed.

    Returns:
        str: A string representing the equation of the tangent line y = a * x + b
             in the format 'a * x + b', where 'a' is the slope and 'b' is the y-intercept,
             both rounded to 2 decimal places (see the examples for a = 0, b = 0,
             a = 1 and a = -1).

    Examples:
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x, 2)
    'x'
    >>> get_tangent(lambda x: -x, 2)
    '- x'
    >>> get_tangent(lambda x: x**2-2, 0.5)
    'x - 2.25'
    >>> get_tangent(lambda x: -x**2-2, 0.5)
    '- x - 1.75'
    """
    df_x0 = round(compute_derivative(func, x_0), 2)

    df_x0_times_x0 = df_x0 * x_0
    f_x0 = func(x_0)

    b = round(-df_x0_times_x0 + f_x0, 2)

    # dfdx(x0)(x - x0) + f(x0)
    res = ''

    a = df_x0
    if a != 0:
        if a < 0:
            res += '- '
        a = abs(a)
        if a not in (0, 1):
            res += f'{a} * '
        res += 'x'

    if b != 0:
        if res:
            res += ' + ' if b > 0 else ' - '
        elif b < 0:
            res = '- '
        res += f'{abs(b)}'
    elif b == 0 and not res:
        res = f'{b}'

    return res


def get_root(func: callable, a: float, b: float) -> float:
    """Compute the root of a function in a given interval.

    The function takes values of different signs at a and b
    and has exactly one root in the interval.

    Args:
        func (callable): The function to evaluate.
        a (float): The start of the interval.
        b (float): The end of the interval.

    Returns:
        float: The root of the function in the interval rounded to 2 decimal places.

    Examples:
    >>> get_root(lambda x: x - 1, 0, 3)
    1.0
    >>> get_root(lambda x: x ** 2 - 2, 0, 2)
    1.41
    """
    epsilon = 0.001
    while abs(f_mid := func(mid := ((a + b) / 2))) > epsilon:
        if f_mid * func(a) < 0:
            b = mid
        elif f_mid * func(b) < 0:
            a = mid
    return round(mid, 2)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
