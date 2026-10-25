"""
Target UA - a word game with Ukrainian words.

The player gets 5 unique Ukrainian letters and a part of speech, and
must name words (up to 5 letters long) of that part of speech that
start and end with one of the given letters.
"""

import random


def generate_grid() -> list[str]:
    """
    Generates a list of 5 unique lowercase Ukrainian letters.

    Returns:
        list[str]: 5 unique letters of the Ukrainian alphabet.
                   Example: ['ґ', 'ь', 'й', 'є', 'ї']

    Examples:
    >>> letters = generate_grid()
    >>> len(letters)
    5
    >>> len(sorted(letters)) == len('абвгґ')
    True
    """

    ukr_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    letters = []
    while len(letters) < 5:
        letter = random.choice(ukr_alphabet)
        if letter not in letters:
            letters.append(letter)
    return letters


def get_words(pathname: str, letters: list[str]) -> list[tuple[str, str]]:
    """
    Reads the dictionary file and returns (word, part_of_speech) pairs
    that match the game rules.

    Dictionary line format: a word, whitespace, then a grammar tag,
    e.g. "абажур /n20.a.p.ke", "аакуватий /adj", "дибки adv".
    The tag (with or without the leading '/') maps to a part of speech:
    'adj...' -> 'adjective', 'adv...' -> 'adverb', 'v...' -> 'verb',
    'noun...' -> 'noun', and 'n' or 'np' followed by a digit -> 'noun'
    (e.g. 'n20.a.p', 'np3'). If a tag lists several parts ("adj.adv"),
    only the first one is used. Lines with any other tags (noninfl,
    numr, conj, prep, ...) are skipped.

    Word selection rules:
    1. Word is at most 5 characters long
    2. Word starts AND ends with one of the letters (they may coincide)
    3. Word's part of speech is one of the four listed above
    Pairs are returned in the order the words appear in the file.

    Args:
        pathname (str): Path to the dictionary file.
        letters (list[str]): 5 lowercase letters of the game grid.

    Returns:
        list[tuple[str, str]]: Pairs (word, part_of_speech).

    Examples:
    >>> import tempfile, os
    >>> content = 'ґедзь /n20.a\\nїдкий /adj.adv\\nдибки adv\\nдіяти /v1\\nщось /pron\\n'
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(content)
    >>> get_words(tmp.name, ['ґ', 'ь', 'й', 'ї', 'и'])
    [('ґедзь', 'noun'), ('їдкий', 'adjective')]
    >>> get_words(tmp.name, ['д', 'и', 'в', 'а', 'я'])
    [('дибки', 'adverb'), ('діяти', 'verb')]
    >>> os.remove(tmp.name)
    """

    words = []
    with open(pathname, mode='r', encoding='utf-8') as dictionary:
        for line in dictionary:
            line = line.split()

            word = line[0]
            if len(word) > 5:
                continue
            if word[0] not in letters or word[-1] not in letters:
                continue

            lang_part = line[1]
            lang_part = lang_part[1:] if lang_part[0] == '/' else lang_part
            if lang_part[0] == 'n' and lang_part[1].isdigit():
                lang_part = 'noun'
            if lang_part[0:2] == 'np' and lang_part[2].isdigit():
                lang_part = 'noun'
            if lang_part.startswith('noun'):
                lang_part = 'noun'
            elif lang_part.startswith('adj'):
                lang_part = 'adjective'
            elif lang_part.startswith('v'):
                lang_part = 'verb'
            elif lang_part.startswith('adv'):
                lang_part = 'adverb'
            else:
                continue

            words.append((word, lang_part))

    return words


def get_user_words() -> list[str]:
    """
    Reads words from user input until EOF signal is received.

    The user enters one word per line. Input is terminated by pressing:
    - Unix/Linux/Mac: Ctrl+D
    - Windows: Ctrl+Z, then Enter

    Returns:
        list[str]: List of words entered by the user.

    Note:
        This function does not print any messages to the screen. All
        instructions for the user should be displayed in the main()
        function.
    """

    words = []
    try:
        while True:
            word = input()
            words.append(word)
    except EOFError:
        return words


def check_user_words(
    user_words: list[str], language_part: str, letters: list[str], vocabulary: str
) -> tuple[list[str], list[str]]:
    """
    Checks user words against the game rules and the dictionary.

    A user word is correct if the pair (word, language_part) matches
    the game rules for the given letters and is present in the
    vocabulary file. Missed words are the dictionary words of the given
    part of speech that match the rules but were not named by the user.

    Args:
        user_words (list[str]): Words entered by the user.
        language_part (str): One of 'noun', 'verb', 'adjective', 'adverb'.
        letters (list[str]): 5 lowercase letters of the game grid.
        vocabulary (str): Path to the dictionary file.

    Returns:
        tuple[list[str], list[str]]: (correct user words, missed words).

    Examples:
    >>> import tempfile, os
    >>> content = 'ґедзь /n20.a\\nїдкий /adj.adv\\nїнь /n20\\nдіяти /v1\\n'
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(content)
    >>> check_user_words(['ґедзь', 'їжак'], 'noun', ['ґ', 'ь', 'й', 'ї', 'и'], tmp.name)
    (['ґедзь'], ['їнь'])
    >>> check_user_words([], 'adjective', ['ґ', 'ь', 'й', 'ї', 'и'], tmp.name)
    ([], ['їдкий'])
    >>> os.remove(tmp.name)
    """

    all_words = get_words(vocabulary, letters)

    guessed = []
    missed = []
    for word, word_lang_part in all_words:
        if word_lang_part != language_part:
            continue
        if word in user_words:
            guessed.append(word)
        else:
            missed.append(word)

    return (guessed, missed)


def main():
    """
    Main function of the Target UA game.

    Implements the complete game scenario:
    1. Generates and displays 5 unique Ukrainian letters
    2. Randomly picks and displays a part of speech
       ('noun', 'verb', 'adjective', 'adverb')
    3. Displays a prompt and reads words from the player
    4. Displays the number of correct words and the list of them
    5. Displays the words that the player missed
    """

    letters = generate_grid()
    print(f'Ваші літери: {' '.join(letters)}')

    lang_parts = ('noun', 'verb', 'adjective', 'adverb')
    lang_part_guess = random.choice(lang_parts)
    print(f'Частина мови: {lang_part_guess}')

    print('Введіть слова (завершення — Ctrl+D):')
    user_words = get_user_words()

    guessed, missed = check_user_words(user_words, lang_part_guess, letters, vocabulary='base.lst')
    print(f'Правильних слів: {len(guessed)}')

    print(f'Ваші правильні слова: {guessed}')
    print(f'Пропущені слова: {missed}')


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
    main()
