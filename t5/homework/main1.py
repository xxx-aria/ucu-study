"""Complete all of the following functions. Currently, they all just
'pass' rather than explicitly return value, meaning they
implicitly return None. They all include doctests, which you can
test by running this file.
The doctests are just examples. Feel free to add your doctests."""


# ****************************************
# Problem 1
# ****************************************
def count_sheep(n):
    """
    Generate a string that counts sheep from 1 to n.

    This function creates a string for counting sheep to help fall asleep.
    For a given non-negative integer n, it returns a string in the format:
    "1 sheep...2 sheep...3 sheep...". Each number is followed by " sheep..."

    If the argument is not a non-negative integer, the function should return None.

    :param n: int, A non-negative integer representing how many sheep to count.
    :return: str or None, The sheep counting string, or None if input is invalid.

    >>> count_sheep(0)
    ''
    >>> count_sheep(1)
    '1 sheep...'
    >>> count_sheep(2)
    '1 sheep...2 sheep...'
    >>> count_sheep(3)
    '1 sheep...2 sheep...3 sheep...'
    >>> count_sheep(-5)
    """
    pass


# ****************************************
# Problem 2
# ****************************************
def remove_vowels(text):
    """
    Remove all vowels from the given string and return the modified string.

    This function removes all vowel characters (a, e, i, o, u, A, E, I, O, U)
    from the input string while preserving all other characters including
    whitespace, punctuation, and the letter 'y'.

    If the argument is not a string, the function should return None.

    :param text: str, The input string from which vowels should be removed.
    :return: str or None, The string without vowels, or None if input is invalid.

    >>> remove_vowels("Hello World!")
    'Hll Wrld!'
    >>> remove_vowels("xyz")
    'xyz'
    >>> remove_vowels("AEIOU")
    ''
    >>> remove_vowels(123) is None
    True
    """
    pass


# ****************************************
# Problem 3
# ****************************************
def round_to_next_five(n):
    """
    Round the given integer to the next (greater than or equal) multiple of 5.

    This function takes an integer and returns the smallest multiple of 5
    that is greater than or equal to the input number. If the input is
    already a multiple of 5, it returns the input unchanged.

    If the argument is not an integer, the function should return None.

    :param n: int, The integer to be rounded.
    :return: int or None, The next multiple of 5, or None if input is invalid.

    >>> round_to_next_five(2)
    5
    >>> round_to_next_five(30)
    30
    >>> round_to_next_five(-2)
    0
    >>> round_to_next_five(3.5) is None
    True
    """
    pass


# ****************************************
# Problem 4
# ****************************************
def hex_char_to_int(c):
    """
    Convert a single hexadecimal character to its integer value (0-15).

    This function takes a single character representing a hexadecimal digit
    (0-9, A-F, a-f) and returns its corresponding integer value from 0 to 15.
    If the character is not a valid hexadecimal digit, the function returns -1.

    This is a helper function useful for parsing hexadecimal color codes.

    If the argument is not a single character string, the function should return None.

    :param c: str, A single character to convert (must be one character long).
    :return: int or None, Integer value 0-15 for valid hex digits, -1 for invalid
                          hex characters, or None if input is invalid.

    >>> hex_char_to_int('0')
    0
    >>> hex_char_to_int('A')
    10
    >>> hex_char_to_int('a')
    10
    >>> hex_char_to_int('#')
    -1
    >>> hex_char_to_int('AB')
    """
    pass


# ****************************************
# Problem 5
# ****************************************
def rot13(message):
    """
    Encode a string using the ROT13 cipher.

    ROT13 is a simple letter substitution cipher that replaces each letter
    with the letter 13 positions after it in the alphabet. It's a special
    case of the Caesar cipher. Since there are 26 letters in the alphabet,
    applying ROT13 twice returns the original text.

    Only letters (A-Z, a-z) are shifted. Numbers, spaces, punctuation, and
    special characters remain unchanged. Case is preserved.

    If the argument is not a string, the function should return None.

    :param message: str, The message to encode with ROT13.
    :return: str or None, The ROT13-encoded message, or None if input is invalid.

    >>> rot13("test")
    'grfg'
    >>> rot13("Hello, World!")
    'Uryyb, Jbeyq!'
    >>> rot13("Why did the chicken cross the road?")
    'Jul qvq gur puvpxra pebff gur ebnq?'
    >>> rot13("123!@# ")
    '123!@# '
    >>> rot13("aBc XyZ")
    'nOp KlM'
    >>> rot13(123)
    """
    pass


# ****************************************
# Problem 6
# ****************************************
def square_digits(n):
    """
    Square every digit of a number and concatenate them into a new integer.

    This function takes an integer, squares each of its digits individually,
    and concatenates the results to form a new integer. For example, the number
    9119 becomes 811181 because 9²=81, 1²=1, 1²=1, 9²=81.

    If the argument is not an integer, the function should return None.
    For negative numbers, the sign is ignored and only digits are processed.

    :param n: int, The integer whose digits should be squared.
    :return: int or None, The new integer formed by concatenating squared digits,
                          or None if input is invalid.

    >>> square_digits(9119)
    811181
    >>> square_digits(0)
    0
    >>> square_digits(5)
    25
    >>> square_digits(3.5)
    """
    pass


# ****************************************
# Problem 7
# ****************************************
def multiply_until_single_digit(num):
    """
    Calculate the multiplicative persistence of a positive integer.

    Multiplicative persistence is the number of times you must multiply
    the digits of a number until you reach a single digit. For example,
    39 has persistence 3 because: 3*9=27, 2*7=14, 1*4=4 (3 steps).

    If the argument is not a non-negative integer, the function should return None.

    :param num: int, A non-negative integer to calculate persistence for.
    :return: int or None, The multiplicative persistence, or None if input is invalid.

    >>> multiply_until_single_digit(39)
    3
    >>> multiply_until_single_digit(999)
    4
    >>> multiply_until_single_digit(4)
    0
    >>> multiply_until_single_digit(-5)
    """
    pass


# ****************************************
# Problem 8
# ****************************************
def find_n_cubes(m):
    """
    Find the number of cubes needed to build a pile with a given total volume.

    This function determines how many cubes are needed to construct a building
    where each cube has a volume that follows the pattern: n³ + (n-1)³ + (n-2)³ + ... + 1³.
    The bottom cube has volume n³, the one above it has volume (n-1)³, and so on
    until the top cube with volume 1³.

    Given the total volume m, the function returns the number n of cubes needed,
    or -1 if no such n exists.

    If the argument is not a positive integer, the function should return None.

    :param m: int, The total volume of the building (must be positive).
    :return: int or None, The number of cubes n, -1 if impossible, or None if input is invalid.

    >>> find_n_cubes(1)
    1
    >>> find_n_cubes(36)
    3
    >>> find_n_cubes(4)
    -1
    >>> find_n_cubes(0)
    """
    pass


# ****************************************
# Problem 9
# ****************************************
def count_carries(num1, num2):
    """
    Count the number of carry operations when adding two numbers.

    A carry operation occurs during addition when the sum of digits in a column
    is 10 or greater, requiring a digit to be transferred to the next column.
    For example, adding 123 + 456: 3+6=9 (no carry), 2+5=7 (no carry), 1+4=5 (no carry).
    But adding 123 + 594: 3+4=7 (no carry), 2+9=11 (1 carry), 1+5+1(carry)=7 (no carry).

    Both numbers should be non-negative integers. The function handles numbers
    of different lengths by zero-padding the shorter one.

    If either argument is not a non-negative integer, the function should return None.

    :param num1: int, The first non-negative integer.
    :param num2: int, The second non-negative integer.
    :return: int or None, The number of carry operations, or None if input is invalid.

    >>> count_carries(123, 456)
    0
    >>> count_carries(555, 555)
    3
    >>> count_carries(9, 99)
    2
    >>> count_carries(1, 9)
    1
    >>> count_carries(-5, 10)
    """
    pass


# ****************************************
# Problem 10
# ****************************************
def collatz_length(n):
    """
    Calculate the length of the Collatz sequence for a given positive integer.

    The Collatz Conjecture states that for any positive natural number n,
    this process:
    - If n is even: divide it by 2
    - If n is odd: multiply it by 3 and add 1
    - Continue until n reaches 1
    will eventually reach n = 1.

    This function returns the number of steps required
    to reach 1, including the initial number and the final 1.

    If the argument is not a positive integer, the function should return None.

    :param n: int, A positive integer to calculate the Collatz sequence length for.
    :return: int or None, The length of the Collatz sequence, or None if input is invalid.

    >>> collatz_length(1)
    1
    >>> collatz_length(2)
    2
    >>> collatz_length(3)
    8
    >>> collatz_length(20)
    8
    >>> collatz_length(0)
    """
    pass


# ****************************************
# Problem 11
# ****************************************
def hex_to_rgb(hex_color):
    """
    Extract the individual RGB (Red, Green, Blue) component values from a hex color.

    This function accepts a hexadecimal color string (case-insensitive) in the
    format "#RRGGBB" and returns a string representation of the RGB values
    in the format "r: R, g: G, b: B" where R, G, and B are integers from 0 to 255.

    The function does not support shorthand hexadecimal notation (e.g., "#FFF").
    You may use the hex_char_to_int() function from Problem 4 to help with conversion.
    For example, for "#FF9933":
    - red is 'FF', that corresponds hex_char_to_int('F')*16+hex_char_to_int('F')
    - green is '99', that corresponds hex_char_to_int('9')*16+hex_char_to_int('9')
    - blue is '33', that corresponds hex_char_to_int('3')*16+hex_char_to_int('3')

    If the argument is not a valid hex color string, the function should return None.

    :param hex_color: str, A hexadecimal color string in format "#RRGGBB".
    :return: str or None, RGB values as "r: R, g: G, b: B", or None if input is invalid.

    >>> hex_to_rgb("#FF9933")
    'r: 255, g: 153, b: 51'
    >>> hex_to_rgb("#000000")
    'r: 0, g: 0, b: 0'
    >>> hex_to_rgb("#AbCdEf")
    'r: 171, g: 205, b: 239'
    >>> hex_to_rgb("#FFF")
    """
    pass


# ****************************************
# Problem 12
# ****************************************
def is_valid_isbn10(isbn):
    """
    Validate an ISBN-10 identifier.

    An ISBN-10 is a 10-character string where the first 9 characters are digits (0-9)
    and the last character can be a digit or 'X' (representing 10).

    An ISBN-10 is valid if the sum of each digit multiplied by its position
    (1-indexed) modulo 11 equals zero:
    (d1*1 + d2*2 + d3*3 + ... + d10*10) % 11 = 0

    If the argument is not a string of exactly 10 characters, the function
    should return None.

    :param isbn: str, A string representing an ISBN-10 identifier.
    :return: bool or None, True if valid ISBN-10, False if invalid format but
                           correct length, or None if input is invalid.

    >>> is_valid_isbn10("1112223339")
    True
    >>> is_valid_isbn10("1112223330")
    False
    >>> is_valid_isbn10("1112223339X")
    >>> is_valid_isbn10(1112223339)
    """
    pass


# ****************************************
# Problem 13
# ****************************************
def prime_factors(n):
    """
    Find the prime factor decomposition of a positive integer n > 1.

    This function returns a string representation of the prime factorization
    in the form "(p1**n1)(p2**n2)...(pk**nk)" where pi are prime factors in
    increasing order and ni are their exponents. If an exponent is 1, it is
    omitted from the output.

    For example: 86240 = 2^5 * 5^1 * 7^2 * 11^1 returns "(2**5)(5)(7**2)(11)"

    If the argument is not an integer greater than 1, the function should return None.

    :param n: int, A positive integer greater than 1.
    :return: str or None, Prime factorization string, or None if input is invalid.

    >>> prime_factors(86240)
    '(2**5)(5)(7**2)(11)'
    >>> prime_factors(2)
    '(2)'
    >>> prime_factors(4)
    '(2**2)'
    >>> prime_factors(100)
    '(2**2)(5**2)'
    >>> prime_factors(7775460)
    '(2**2)(3**3)(5)(7)(11**2)(17)'
    >>> prime_factors(1)
    >>> prime_factors(0)
    """
    pass


# ****************************************
# Problem 14
# ****************************************
def reduce_fraction(numerator, denominator):
    """
    Reduce a fraction to its simplest form and return it as a string.

    Don't use recursion! Investigate the Euclidean algorithm.
    This function takes a numerator and denominator as positive integers
    and returns the fraction reduced to its lowest terms in the format
    'numerator/denominator'. The function finds the greatest common divisor
    (GCD) of both numbers and divides them by it.

    If either argument is not a positive integer, the function should return None.

    :param numerator: int, The numerator of the fraction (must be positive).
    :param denominator: int, The denominator of the fraction (must be positive).
    :return: str or None, The reduced fraction as a string, or None if input is invalid.

    >>> reduce_fraction(45, 120)
    '3/8'
    >>> reduce_fraction(10, 5)
    '2/1'
    >>> reduce_fraction(7, 13)
    '7/13'
    >>> reduce_fraction(5, 0)
    """
    pass


# ****************************************
# Problem 15
# ****************************************
def to_binary(n):
    """
    Convert a non-negative integer to its binary representation as a string.

    This function converts a decimal number to binary without using
    the built-in bin() function. The result contains no '0b' prefix
    and no leading zeros.

    If the argument is not a non-negative integer, the function should return None.

    :param n: int, A non-negative integer to convert.
    :return: str or None, The binary representation, or None if input is invalid.

    >>> to_binary(0)
    '0'
    >>> to_binary(1)
    '1'
    >>> to_binary(5)
    '101'
    >>> to_binary(64)
    '1000000'
    >>> to_binary(255)
    '11111111'
    >>> to_binary(-3)
    >>> to_binary(2.5)
    """
    pass


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
