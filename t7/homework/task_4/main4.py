"""
Eternas - a 3D "four in a row" strategy game on a circular board.

There are 16 pegs arranged in a circle; up to 4 beads can be put on
each peg. Beads are green ('g') or white ('w'); 0 marks an empty slot.
The first player to place four beads of their colour in a row
vertically, horizontally or diagonally wins, and the game stops.
"""

import random


def check_one_colour(beads: list[str | int]) -> bool:
    """Checks if 4 beads are of one colour."""
    return beads.count('w') == 4 or beads.count('g') == 4


def check_verticals(
    board: list[list[str | int]],
) -> bool | tuple[bool | list[list[tuple[int, int]]]]:
    """Looks for up verticals of one colour."""

    combinations = []

    for peg_i in range(16):
        if check_one_colour(board[peg_i]):
            combinations.append([(j, peg_i) for j in range(4)])

    return combinations


def check_horizontals(
    board: list[list[str | int]],
) -> bool | tuple[bool | list[list[tuple[int, int]]]]:
    """Look for horizontals of one colour."""

    combinations = []
    rows = [[board[j][i] for j in range(16)] for i in range(4)]

    for row_i in range(4):
        for peg_i in range(16):
            row_slice = [rows[row_i][i % 16] for i in range(peg_i, peg_i + 4)]

            if check_one_colour(row_slice):
                combinations.append([(row_i, i % 16) for i in range(peg_i, peg_i + 4)])

    return combinations


def check_diag_down(
    board: list[list[str | int]],
) -> bool | tuple[bool | list[list[tuple[int, int]]]]:
    """Looks for down diagonals of one colour."""

    combinations = []

    for peg_i in range(-3, 13):
        diag_down = [board[peg_i + x][3 - x] for x in range(4)]
        if check_one_colour(diag_down):
            combinations.append([(3 - x, peg_i + x) for x in range(4)])

    return combinations


def check_diag_up(board: list[list[str | int]]) -> bool | tuple[bool | list[list[tuple[int, int]]]]:
    """Looks for up diagonals of one colour."""

    combinations = []

    for peg_i in range(-3, 13):
        diag_down = [board[peg_i + x][x] for x in range(4)]
        if check_one_colour(diag_down):
            combinations.append([(x, peg_i + x) for x in range(4)])

    return combinations


def winning_combination(
    board: list[list[str | int]],
) -> bool | tuple[bool | list[list[tuple[int, int]]]]:
    """
    Checks the board for winning combinations.

    Returns False if there is none. Otherwise returns a tuple
    (True, combinations) where combinations is a list of lists of
    4 positions (level, peg): level 0..3 is the index inside the peg
    list, peg 0..15 is the peg index.

    The board is circular, so horizontal and diagonal combinations
    wrap around peg 15 back to peg 0. Positions in a combination are
    listed left to right (peg index ascending along the combination)
    and top to bottom for the vertical case. Combinations are listed
    in this order: vertical, then horizontal (level by level, start
    peg ascending), then "down" diagonals (start peg ascending), then
    "up" diagonals (start peg ascending).

    Args:
        board (list[list]): 16 lists of 4 items ('g', 'w' or 0).

    Returns:
        bool | tuple[bool, list[list[tuple[int, int]]]]

    Examples:
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], \
['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], \
[0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], \
[0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], \
[0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 0, 'g', 'w'], \
[0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'w', 'g'], \
[0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> board = [['g', 'g', 'g', 'g']] + [[0, 0, 0, 0] for _ in range(15)]
    >>> winning_combination(board)
    (True, [[(0, 0), (1, 0), (2, 0), (3, 0)]])
    """

    combinations = []
    combinations.extend(check_verticals(board))
    combinations.extend(check_horizontals(board))
    combinations.extend(check_diag_down(board))
    combinations.extend(check_diag_up(board))

    if combinations:
        return (True, combinations)
    return False


def put_bead(board: list[list[str | int]], color: str, peg: int) -> None:
    """Puts a coloured bead on the requested peg of the board."""

    for i in range(3, -1, -1):
        if board[peg][i] == 0:
            board[peg][i] = color


def board_generation() -> list[list[str | int]]:
    """
    Generates a random legal position of the Eternas game.

    Returns a list of 16 lists of 4 items each. Each item is 'g'
    (green bead), 'w' (white bead) or 0 (empty slot). Beads are put
    on a peg from the end of its list (index 3 is the first bead),
    so inside every peg list all 0s come before the beads.

    The position must be reachable in a real game:
    - at most 16 beads of each colour;
    - players move in turn, so the difference between the number of
      green and white beads is at most 1;
    - the game stops as soon as a winning combination appears, so a
      board may contain winning combinations only if they all share
      the bead placed by the very last move.

    Returns:
        list[list]: the generated board.

    Examples:
    >>> board = board_generation()
    >>> len(board)
    16
    >>> [len(peg) for peg in board] == [4] * 16
    True
    >>> [item for peg in board for item in peg if item not in (0, 'g', 'w')]
    []
    """

    board = [[0] * 4 for _ in range(16)]
    available_pegs = list(range(16))
    moves = random.randint(1, 32)

    for move in range(moves):
        color = 'g' if move % 2 == 1 else 'w'
        peg = random.choice(available_pegs)
        put_bead(board, color, peg)
        if board[peg].count(0) == 0:
            available_pegs.remove(peg)
        if winning_combination(board)[0]:
            break

    return board


def save_board(board: list[list[str | int]], pathname: str) -> None:
    """
    Saves the board to a text file.

    Writes 16 lines, one per peg, in peg order. Each line holds the
    4 items of the peg list (level 0 to 3) separated by single
    spaces, e.g. "0 0 g w". The function returns nothing.

    Args:
        board (list[list]): 16 lists of 4 items ('g', 'w' or 0).
        pathname (str): path to the output file.

    Examples:
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as out:
    ...     pass
    >>> board = [[0, 0, 0, 0] for _ in range(16)]
    >>> board[2] = [0, 0, 'g', 'w']
    >>> save_board(board, out.name)
    >>> with open(out.name, encoding='utf-8') as src:
    ...     lines = src.read().split('\\n')
    >>> lines[2]
    '0 0 g w'
    >>> lines[15]
    '0 0 0 0'
    >>> os.remove(out.name)
    """
    with open(pathname, mode='w', encoding='utf-8') as board_file:
        board_file.writelines([' '.join([str(bead) for bead in peg]) + '\n' for peg in board])


def read_board(pathname: str) -> list[list[str | int]]:
    """
    Reads a board from a text file written in the save_board format.

    The file holds 16 lines, one per peg; each line has the 4 items
    of the peg list (level 0 to 3) separated by spaces: 'g', 'w'
    or 0. Returns the board as a list of 16 lists of 4 items; empty
    slots are the integer 0, not the string '0'.

    Args:
        pathname (str): path to the input file.

    Returns:
        list[list]: the board read from the file.

    Examples:
    >>> import tempfile, os
    >>> content = '\\n'.join(['0 0 g w'] + ['0 0 0 0'] * 15)
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(content)
    >>> board = read_board(tmp.name)
    >>> board[0]
    [0, 0, 'g', 'w']
    >>> board[1]
    [0, 0, 0, 0]
    >>> len(board)
    16
    >>> os.remove(tmp.name)
    """

    board = []
    with open(pathname, mode='r', encoding='utf-8') as board_file:
        for peg in board_file:
            board.append([int(bead) if bead == '0' else bead for bead in peg.split()])

    return board


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
