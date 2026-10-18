"""My lab"""


def is_num(num: str) -> bool:
    """
    Check whether string could be converted into number.

    >>> is_num('0')
    True
    >>> is_num('-10')
    True
    >>> is_num('а1')
    False
    >>> is_num('')
    False
    """
    if len(num) == 0:
        return False
    return num.isdigit() or (num[0] == '-' and num[1:].isdigit())


def calculate_expression(expression: str) -> int | str:
    """
    Calculate numerical result of the given textual representation of the math expression.

    Is capable of calculating addition, subtraction, division, and multiplication
    of single or complex expression, but operations priority is not considered.

    Return 'Неправильний вираз!' if input is invalid.
    Input is considered invalid if expression
    does not follow correct format ("Скільки буде ...  ?"),
    or requested expression's difficulty is beyond functionality,
    or ZeroDivisionError occurs.

    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 7 додати 3 помножити на 5?')
    50
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression('Скільки буде 3 в кубі?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки сезонів у році?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2 2 додати?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 5?')
    5
    >>> calculate_expression('Скільки буде ?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 1 додати?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 1 помножити на?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 5 поділити на 0?')
    'Неправильний вираз!'
    """

    if not (expression.startswith('Скільки буде ') and expression[-1] == '?'):
        return 'Неправильний вираз!'

    expr = expression[:-1].split(' ')[2:]
    operations = ('додати', 'плюс', 'відняти', 'мінус', 'помножити на', 'поділити на')

    if not is_num(expr[0]):
        return 'Неправильний вираз!'
    result = int(expr[0])

    i = 0
    while i <= len(expr) - 2:
        op = expr[i + 1]
        if i + 2 < len(expr) and expr[i + 2] == 'на':
            op += ' ' + expr[i + 2]
            i += 1
        i += 1

        if i >= len(expr) - 1:
            return 'Неправильний вираз!'

        curr_num = expr[i + 1]

        if not is_num(curr_num) or op not in operations:
            return 'Неправильний вираз!'

        curr_num = int(curr_num)

        match op:
            case 'додати' | 'плюс':
                result += curr_num
            case 'відняти' | 'мінус':
                result -= curr_num
            case 'помножити на':
                result *= curr_num
            case 'поділити на':
                try:
                    result //= curr_num
                except ZeroDivisionError:
                    return 'Неправильний вираз!'

        i += 1

    return result


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
