def calculate_expression(expression: str) -> int | None:
    """
    Calculate numerical result of the given textual expression.

    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 7 додати 3 помножити на 5?')
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression('Скільки буде 3 в кубі?')
    'Неправильний вираз!'
    """

    # is_valid = True ?

    if not isinstance(expression, str):
        return 'Неправильний вираз!'

    if not (expression.startswith('Скільки буде ') and expression[::-1].startswith('?')):#endswith
        return 'Неправильний вираз!'

    expr = expression[:-1].split(' ')[2:]

    operations = ('додати плюс', 'відняти мінус', 'помножити на', 'поділити на')

    for unit in expr:
        if unit.isdigit():
            ...

    return expr

print(calculate_expression('faefwwf'))
print(calculate_expression('Скільки буде 7 додати 3 помножити на 5?'))
print(calculate_expression('Скільки буде 3 додати 2?'))
# if '__name__' == '__main__':
#     import doctest
#     doctest.testmod()
