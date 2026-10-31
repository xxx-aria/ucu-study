"""
CMU pronouncing dictionary: reading it from a file into a list or
a dictionary and grouping words by the number of their pronunciations.
"""


def dict_reader_tuple(file_dict: str) -> list:
    """
    Reads a pronunciation dictionary file and returns a list of tuples.

    Each line of the file holds a word, the number of its pronunciation
    variant and the phonemes, separated by spaces, e.g.
        NACHOS 2 N AE1 CH OW0 Z
    Every line becomes a tuple (word, variant, phonemes), where word is
    a str, variant is an int and phonemes is a list of str. The tuples
    go in the same order as the lines in the file.

    Parameters:
    -----------
    file_dict : str
        The path to the pronunciation dictionary file.

    Returns:
    --------
    list[tuple[str, int, list[str]]]:
        A list of tuples (word, variant number, phonemes).

    Example:
    --------
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
    ...                                  encoding='utf-8') as tmp:
    ...     _ = tmp.write('A 1 AH0\\nA. 1 EY1\\nA 2 EY1\\nNACHOS 1 N AA1 CH OW0 Z\\n')
    >>> dict_reader_tuple(tmp.name)[2]
    ('A', 2, ['EY1'])
    >>> dict_reader_tuple(tmp.name)[3]
    ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z'])
    >>> len(dict_reader_tuple(tmp.name))
    4
    >>> os.remove(tmp.name)
    """

    words = []
    with open(file_dict, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            if len(line) < 3:
                continue
            word, num = line[0], int(line[1])
            phonemes = line[2:]
            words.append((word, num, phonemes))

    return words


def dict_reader_dict(file_dict: str) -> dict:
    """
    Reads a pronunciation dictionary file and returns a dictionary.

    Each word is a key in the dictionary, and the value is a set of
    tuples of phonemes: one tuple for each pronunciation of the word.

    Parameters:
    -----------
    file_dict : str
        The path to the pronunciation dictionary file.

    Returns:
    --------
    dict[str, set[tuple[str, ...]]]:
        A dictionary where each key is a word and the value is a set
        of phoneme tuples.

    Example:
    --------
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
    ...                                  encoding='utf-8') as tmp:
    ...     _ = tmp.write('A 1 AH0\\nA. 1 EY1\\nA 2 EY1\\nNACHOS 1 N AA1 CH OW0 Z\\n')
    >>> dict_reader_dict(tmp.name)['A'] == {('AH0',), ('EY1',)}
    True
    >>> dict_reader_dict(tmp.name)['NACHOS']
    {('N', 'AA1', 'CH', 'OW0', 'Z')}
    >>> len(dict_reader_dict(tmp.name))
    3
    >>> os.remove(tmp.name)
    """

    words = {}
    with open(file_dict, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            if len(line) < 3:
                continue
            word = line[0]
            phonemes = line[2:]
            if word not in words:
                words[word] = set()
            words[word].add(tuple(phonemes))

    return words


def dict_invert(dct) -> dict:
    """
    Groups the words of a pronunciation dictionary by the number of
    their pronunciations.

    The input is either a list of tuples (the result of
    dict_reader_tuple) or a dictionary (the result of dict_reader_dict).
    The result is a dictionary: each key is a number of pronunciations,
    the value is a set of tuples (word, phonemes) for all words with
    exactly that many pronunciations; phonemes are a tuple of str.
    A word with n pronunciations gives n such tuples. The keys of the
    result go in ascending order.

    Parameters:
    -----------
    dct : dict or list
        The pronunciation dictionary in dictionary or list format.

    Returns:
    --------
    dict[int, set[tuple[str, tuple[str, ...]]]]:
        A dictionary from the number of pronunciations to the set of
        (word, phonemes) tuples.

    Example:
    --------
    >>> dict_invert({'WATER': {('W', 'A', 'T', 'E', 'R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    >>> dict_invert([('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'])])
    {1: {('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'))}}
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},
    ...              'A': {('EY1',), ('AH0',)}}) == {
    ...     1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G'))},
    ...     2: {('A', ('EY1',)), ('A', ('AH0',))}}
    True
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
    ...                                  encoding='utf-8') as tmp:
    ...     _ = tmp.write('A 1 AH0\\nA. 1 EY1\\nA 2 EY1\\nNACHOS 1 N AA1 CH OW0 Z\\n')
    >>> dict_invert(dict_reader_tuple(tmp.name)) == dict_invert(dict_reader_dict(tmp.name))
    True
    >>> os.remove(tmp.name)
    """

    dct_dict = dct
    if isinstance(dct, list):
        dct_dict = {}
        for word, _, phonemes in dct:
            if word not in dct_dict:
                dct_dict[word] = set()
            dct_dict[word].add(tuple(phonemes))

    dct_by_freq = {}
    for word, prns in dct_dict.items():
        num = len(prns)
        if num not in dct_by_freq:
            dct_by_freq[num] = set()
        for pronunciation in prns:
            dct_by_freq[num].add((word, tuple(pronunciation)))

    # in ascending order 1, 2, 3 ...
    res = {}
    for num in sorted(dct_by_freq):
        res[num] = dct_by_freq[num]

    return res


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
