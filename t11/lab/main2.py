"""
Модуль fibonacci_factorial: факторіал і числа Фібоначчі
рекурсивно та ітеративно, порівняння часу виконання.
"""

import time


def measure_time(func):
    '''Measures time.'''

    def wrapper(n):
        t0 = time.time()
        res = func(n)
        func_t = time.time() - t0
        print(f'{func_t} s')
        return res

    return wrapper


def factorial_recursive(n: int) -> int:
    """
    Return n! for a non-negative integer n. Works recursively.

    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(3)
    6
    >>> factorial_recursive(7)
    5040
    """
    if n <= 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Return n! for a non-negative integer n. Works iteratively.

    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(3)
    6
    >>> factorial_iterative(7)
    5040
    """
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res


def fibonacci_recursive(n: int) -> int:
    """
    Return the n-th Fibonacci number (the sequence 1, 1, 2, 3, 5, ...,
    indices start from 0). Works recursively.

    >>> fibonacci_recursive(0)
    1
    >>> fibonacci_recursive(1)
    1
    >>> fibonacci_recursive(5)
    8
    >>> fibonacci_recursive(9)
    55
    """
    if n <= 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Return the n-th Fibonacci number (the sequence 1, 1, 2, 3, 5, ...,
    indices start from 0). Works iteratively.

    >>> fibonacci_iterative(0)
    1
    >>> fibonacci_iterative(1)
    1
    >>> fibonacci_iterative(5)
    8
    >>> fibonacci_iterative(50)
    20365011074
    """
    nums = []
    for i in range(n + 1):
        if i in (0, 1):
            nums += [1]
            continue
        nums += [nums[i - 1] + nums[i - 2]]
    return nums[n]


def time_test(function, n: int, verbose: bool = False) -> float:
    """
    Run function(n) and return the time it took in seconds.
    If verbose is True, also print additional information
    (what exactly, you decide yourself).
    """
    t0 = time.time()
    function(n)
    func_t = time.time() - t0
    if verbose:
        print(f'function {function.__name__} took {func_t}s')
        if function in (factorial_recursive, fibonacci_recursive):
            print(f'number of recursive calls = {n + 1}')
    return func_t


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
