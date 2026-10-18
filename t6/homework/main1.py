"""My lab"""


def insert_dyvo(sentence: str, flag: str) -> str:
    """
    Inserting word "диво" before every word that starts with flag.

    Inserted "диво" should match the case of the first letter
    of the word it is prepended to.
    So it is either capitalized, or in lowercase.

    Matching for both flag and words is not case sensitive.

    >>> insert_dyvo('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> insert_dyvo('Світлий день у цьому Світі настав цим свіжим літом.', 'сві')
    'Дивосвітлий день у цьому Дивосвіті настав цим дивосвіжим літом.'
    >>> insert_dyvo('', 'ки')
    ''
    >>> insert_dyvo('Наступні кілька днів буде йти дощ.', 'ки')
    'Наступні кілька днів буде йти дощ.'
    >>> insert_dyvo('ЛІТО У  ЛІСІ', 'лі')
    'ДиволІТО У  ДиволІСІ'
    >>> insert_dyvo('Кит пливе', 'КИ')
    'Дивокит пливе'
    """

    res_words = []
    for word in sentence.split(' '):
        if word and word.lower().startswith(flag.lower()):
            prefix = 'диво'
            if word[0].isupper():
                prefix = prefix.capitalize()
                word = word[0].lower() + word[1:]
            word = prefix + word
        res_words.append(word)

    return ' '.join(res_words)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
