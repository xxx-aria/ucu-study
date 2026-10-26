"""
Target Game - a word search game using letters from the game grid.

The player must find as many words as possible (minimum 4 letters) using
letters from a 3x3 grid. Each word must contain the central letter.
"""

import random


def generate_grid() -> list[list[str]]:
    """
    Generates a 3x3 grid of uppercase letters for the game.

    The grid should contain 3 vowels and 6 consonants for optimal game
    balance.

    Returns:
        list[list[str]]: A list of 3 lists, each containing 3 uppercase letters.
                         Example: [['E', 'T', 'O'], ['O', 'P', 'N'], ['P', 'U', 'R']]

    Examples:
    >>> grid = generate_grid()
    >>> len(grid)
    3
    >>> [len(row) for row in grid]
    [3, 3, 3]
    >>> len([letter for row in grid for letter in row])
    9
    """

    n = 3
    vowels_left = 3
    consonants_left = 6
    grid = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            while True:
                letter = random.choice(range(ord('A'), (ord('Z') + 1)))
                letter = chr(letter)
                if letter in ('A', 'E', 'I', 'O', 'U') and vowels_left > 0:
                    vowels_left -= 1
                    break
                if letter not in ('A', 'E', 'I', 'O', 'U') and consonants_left > 0:
                    consonants_left -= 1
                    break
            grid[i][j] = letter

    return grid


def word_is_valid(word: str, letters: list[str]) -> bool:
    """
    Checks whether the word meets game's constraints.

    Word constraints:
    1. Word must contain at least 4 letters
    2. Word must contain the central letter
    3. Each letter in the word is used no more times than it appears on the grid
    4. All letters in the word must be present on the grid

    Returns:
        bool: True if word is valid, False if not.

    Note:
        Does not check the peresence in the dictionary.
    """

    central_letter = letters[4]
    if len(word) < 4:
        return False
    if central_letter not in word:
        return False
    for letter in word:
        if word.count(letter) > letters.count(letter):
            return False
    return True


def get_words(pathname: str, letters: list[str]) -> list[str]:
    """
    Reads the dictionary file and returns words that match the game rules.

    Word selection rules:
    1. Word must contain at least 4 letters
    2. Word must contain the central letter
    3. Each letter in the word is used no more times than it appears on the grid
    4. All letters in the word must be present on the grid
    5. Words are returned in lowercase

    Args:
        pathname (str): Path to the dictionary file
        letters (list[str]): List of 9 letters from the game grid in lowercase.
                             Element at index 4 is the central letter (mandatory).
                             Example: ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r']

    Returns:
        list[str]: List of words from the dictionary that match all rules.

    Examples:
        >>> get_words('en.txt', ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f'])[:8]
        ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok']
        >>> len(get_words('en.txt', ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f']))
        16
        >>> words = get_words('en.txt', ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r'])
        >>> [word for word in words if 'p' not in word]
        []
        >>> [word for word in words if len(word) < 4]
        []
    """

    valid_words = []

    with open(pathname, mode='r', encoding='utf-8') as dictionary:
        for word in dictionary:
            word = word.strip().lower()
            if word_is_valid(word, letters) and word not in valid_words:
                valid_words.append(word)

    return valid_words


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
        instructions for the user should be displayed in the main() function.
    """

    words = []
    try:
        while True:
            word = input()
            words.append(word)
    except EOFError:
        return words


def get_pure_user_words(
    user_words: list[str], letters: list[str], words_from_dict: list[str]
) -> list[str]:
    """
    Checks user words and returns those that match game rules but are not in the dictionary.

    This function helps identify words that the user entered correctly according
    to the game rules (length >= 4, contain central letter, all letters are on
    the grid), but which were not found in the game dictionary. These could be
    spelling errors or rare words.

    Args:
        user_words (list[str]): Words entered by the user.
        letters (list[str]): List of 9 letters from the game grid (lowercase).
                             Element [4] is the central letter.
        words_from_dict (list[str]): Words from the dictionary that match the rules.

    Returns:
        list[str]: List of user words that match game rules but are not found
                   in the dictionary.

    Examples:
        >>> letters = ['i', 'g', 'e', 'p', 'i', 's', 'w', 'm', 'g']
        >>> get_pure_user_words(['impi', 'gipm'], letters, ['work', 'worm'])
        ['impi', 'gipm']
        >>> get_pure_user_words(['test'], ['i', 'g', 'e', 'p', 'i', 's', 'w', 'm', 'g'], [])
        []
        >>> get_pure_user_words(['pig'], ['p', 'i', 'g', 'e', 'p', 's', 'w', 'm', 'g'], [])
        []
    """

    valid_words = []
    for word in user_words:
        if word not in words_from_dict and word_is_valid(word, letters):
            valid_words.append(word)

    return valid_words


def main():
    """
    Main function of the Target game.

    Implements the complete game scenario:
    1. Generates and displays a 3x3 game grid
    2. Displays a prompt and reads words from the player
    3. Gets all possible words from the dictionary
    4. Displays the number of correct words from the user
    5. Displays all possible words from the dictionary
    6. Displays words that the player missed
    7. Displays player's words that are not in the dictionary
    """

    grid = generate_grid()
    print('\n'.join([' '.join(row) for row in grid]))

    letters = [letter.lower() for row in grid for letter in row]
    all_words = get_words('en.txt', letters)

    print('Введіть слова (завершення — Ctrl+D):')
    user_words = get_user_words()

    correct_counter = 0
    skipped_words = []
    for word in all_words:
        if word in user_words:
            correct_counter += 1
        else:
            skipped_words.append(word)
    print(f'Правильних слів: {correct_counter}')

    print(f'Усі можливі слова: {all_words}')
    print(f'Пропущені слова: {skipped_words}')

    extra_words = get_pure_user_words(user_words, letters, all_words)
    print(f'Слова поза словником: {extra_words}')


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
    main()
