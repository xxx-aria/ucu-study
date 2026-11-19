"""
Модуль happy: пошук щасливих трамвайних квитків.

Номер квитка доповнюється нулями зліва до 8 цифр.
Квиток щасливий, якщо цифровий корінь суми перших чотирьох цифр
дорівнює цифровому кореню суми останніх чотирьох цифр.
"""


def digital_root(digits: str) -> int:
    """
    Return the digital root of a string of digits: the digits are
    summed repeatedly until a single digit remains.
    The function must be recursive.

    >>> digital_root('0000')
    0
    >>> digital_root('7')
    7
    >>> digital_root('2345')
    5
    >>> digital_root('0015')
    6
    """
    if len(digits) <= 1:
        return int(digits)
    return digital_root(str(sum(int(digit) for digit in digits)))


def happy_number(num: int) -> bool:
    """
    Return True if the ticket with number num is lucky, False otherwise.
    The number is padded with zeros on the left to 8 digits.

    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    >>> happy_number(10001)
    True
    """
    num_str = str(num)
    num_str = '0' * (8 - len(num_str)) + num_str
    return digital_root(num_str[:4]) == (digital_root(num_str[4:]))


def count_happy_numbers(n: int) -> int:
    """
    Return the number of lucky tickets among the numbers from 1 to n inclusive.
    Use a generator expression.

    >>> count_happy_numbers(10000)
    0
    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    """
    nums = (num for num in range(1, n + 1))
    nums_is_happy = map(happy_number, nums)
    return sum(nums_is_happy)


def happy_numbers(m: int, n: int) -> list[int]:
    """
    Return the list of lucky tickets among the numbers from m to n inclusive.
    Use a list comprehension.

    >>> happy_numbers(1, 11)
    []
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(10001, 10030)
    [10001, 10010, 10019, 10028]
    """
    # nums = [num for num in range(m, n + 1)]
    # return list(filter(happy_number, nums))
    return [num for num in range(m, n + 1) if happy_number(num)]


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
