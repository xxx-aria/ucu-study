def is_isogram(word):
    """
    Docstring for is_isogram

    :param word: Description

    >>> is_isogram("isogram")
    True
    >>> is_isogram("aba")
    False
    >>> is_isogram("moOse")
    False
    """
    letters = {}
    for l in word:
        l = l.lower()
        count = letters.get(l, 0)
        if count > 0:
            return False
        letters.setdefault(l, count + 1)
    return True


def char_to_ascii(word):
    """
    Docstring for char_to_ascii

    :param word: Description

    >>> char_to_ascii("a")
    {'a': 97}
    >>> char_to_ascii("aaa")
    {'a': 97}
    >>> char_to_ascii("hello world")
    757
    """
    letters = {}
    for l in word:
        if l.isalpha():
            letters[l] = ord(l)

    if len(letters) > 1:
        return sum(letters.values())
    return letters


def scramble(str1, str2):
    """
    Docstring for scramble

    :param str1: Description
    :param str2: Description

    >>> scramble('rkqodlw', 'world')
    True
    >>> scramble('katas', 'steak')
    False
    """

    l1 = {}
    l2 = {}
    for l in str1:
        l1[l] = str1.count(l)
    for l in str2:
        l2[l] = str2.count(l)

    for k, v in l2.items():
        if l1.get(k, 0) == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
