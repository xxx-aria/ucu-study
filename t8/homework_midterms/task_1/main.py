"""Chess game."""


def read_board(filename: str) -> list:
    """
    Reads a chess board configuration from a file and returns it as a 2D list.
    Each line consists of 8 characters representing the pieces or empty squares.

    Piece Representation:
    - Uppercase letters represent white pieces.
    - Lowercase letters represent black pieces.
    - '.' represents an empty square.

    Piece Notation:
    - 'P' or 'p': Pawn
    - 'R' or 'r': Rook
    - 'N' or 'n': Knight
    - 'B' or 'b': Bishop
    - 'Q' or 'q': Queen
    - 'K' or 'k': King

    Coordinate System:
    - The board is an 8x8 grid.
    - The bottom-left corner (square 'a1') corresponds to coordinates (0, 0).
    - The top-right corner (square 'h8') corresponds to coordinates (7, 7).

    Parameters:
    -----------
    filename : str
        The path to the file containing the chess board configuration.

    Returns:
    --------
    list[list[str]]:
        A 2D list representing the chessboard, where each inner list is a row,
        and each element is a character representing a piece or an empty square.

    Example:
    --------
    >>> board = read_board("chess_board.txt")
    >>> board
    [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],\
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', 'P'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    """
    board = [] * 8
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split('\n')
        board = [list(line) for line in lines[::-1]]

    return board


def square_to_coordinate(square: str) -> tuple:
    """
    Converts a chess square notation to board coordinates.

    Parameters:
    -----------
    square : str
        The square in game board notation (e.g., 'e4').

    Returns:
    --------
    tuple[int, int]:
        A tuple (row_index, column_index) representing the position on the board.

    Example:
    --------
    >>> square_to_coordinate('a4')
    (3, 0)
    >>> square_to_coordinate('e5')
    (4, 4)
    """
    row = int(square[1]) - 1
    col = ord(square[0].lower()) - ord('a')
    return (row, col)


def get_move(board: list, move: tuple) -> tuple:
    """
    Calculates the result of moving a piece on the board without modifying the board.

    Parameters:
    -----------
    - board: list[list[str]]
        The current state of the chessboard.
    - move: tuple[str, str, int]
        The move to perform:
        - move[0]: str
            Starting square in chess board notation (e.g., 'e2').
        - move[1]: str
            Direction of movement ('U', 'D', 'L', 'R', 'UR', 'UL', 'DR', 'DL', 'N').
        - move[2]: int
            Number of steps to move (or specific code for knight moves).

    Returns:
    -----------
    - tuple[str, tuple[int, int], str]:
        - The figure to move.
        - The end coordinates as a tuple (row_index, column_index).
        - The piece at the destination square (captured piece), or
          '.' if empty, or '' if out of bounds.

    Directions:
    -----------
    - 'U': Up (increase row index).
    - 'D': Down (decrease row index).
    - 'L': Left (decrease column index).
    - 'R': Right (increase column index).
    - 'UR': Up-Right diagonal.
    - 'UL': Up-Left diagonal.
    - 'DR': Down-Right diagonal.
    - 'DL': Down-Left diagonal.
    - 'N': Knight moves, with move[2] specifying the move:
        1. Up 2, Left 1
        2. Up 1, Left 2
        3. Down 1, Left 2
        4. Down 2, Left 1
        5. Down 2, Right 1
        6. Down 1, Right 2
        7. Up 1, Right 2
        8. Up 2, Right 1

    Example:
    --------
    >>> board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],\
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', 'P'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    >>> board[1][4]
    'P'
    >>> get_move(board, ("e2", "U", 2))
    ('P', (3, 4), '.')
    >>> get_move(board, ("e2", "D", 2))
    ('P', (-1, 4), '')
    >>> get_move(board, ("d8", "DR", 4))
    ('q', (3, 7), 'P')
    >>> get_move(board, ("g1", "N", 1))
    ('N', (2, 5), '.')
    """
    row, col = square_to_coordinate(move[0])
    figure = board[row][col]

    units = move[2]
    if 'U' in move[1]:
        row += units
    if 'D' in move[1]:
        row -= units
    if 'R' in move[1]:
        col += units
    if 'L' in move[1]:
        col -= units
    if move[1] == 'N':
        if units in (1, 4, 5, 8):
            col += -1 + 2 * (units > 4)  # -1 or 1
        if units in (2, 3, 6, 7):
            col += -2 + 4 * (units > 3)  # -2 or 2
        if units in (3, 6, 2, 7):
            row += +1 - 2 * (2 < units < 7)
        if units in (1, 8, 4, 5):
            row += +2 - 4 * (1 < units < 8)

    dest = board[row][col] if 0 <= row < 8 and 0 <= col < 8 else ''
    return (figure, (row, col), dest)


def make_move(board: list, move: tuple) -> list | None:
    """
    Attempts to make a move on the board, returning a new board if valid.

    Validity Conditions:
    --------
    - The starting square contains a piece (not empty).
    - The destination square is within the board boundaries.
    - The move results in capturing an opponent's piece or moving to an empty square.
    - Cannot capture a piece of the same color.

    Parameters:
    --------
    - board: list[list[str]]
        The current state of the chessboard.
    - move: tuple[str, str, int]
        The move to perform:
        - move[0]: str
            Starting square in algebraic notation (e.g., 'e2').
        - move[1]: str
            Direction of movement ('U', 'D', 'L', 'R', 'UR', 'UL', 'DR', 'DL', 'N').
        - move[2]: int
            Number of steps to move (or specific code for knight moves).

    Returns:
    --------
    - list[list[str]]:
        A new board with the move made if valid.
    - None:
        If the move is invalid.

    Notes:
    - Assumes pieces can move over other pieces without obstruction.

    Example:
    --------
    >>> board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],\
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', 'P'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    >>> board[1][4]
    'P'
    >>> new_board = make_move(board, ("e2", "U", 2))
    >>> new_board[1][4]
    '.'
    >>> board[1][4]
    'P'
    >>> new_board[3][4]
    'P'
    >>> new_board = make_move(new_board, ("d8", "DR", 4))
    >>> new_board[7][3]
    '.'
    >>> new_board[3][7]
    'q'
    >>> new_board= make_move(board, ("g1", "N", 1))
    >>> board[0][6]
    'N'
    >>> board[2][5]
    '.'
    >>> new_board[2][5]
    'N'
    >>> new_board[0][6]
    '.'
    >>> new_board = make_move(board, ("e2", "D", 2))
    >>> new_board is None
    True
    """
    row_0, col_0 = square_to_coordinate(move[0])
    if board[row_0][col_0] == '.':
        return None

    figure, row_col, dest = get_move(board, move)
    row, col = row_col
    if not dest:
        return None

    if figure.isupper() and dest.isupper():
        return None
    if figure.islower() and dest.islower():
        return None

    board = [row[:] for row in board]
    board[row_0][col_0] = '.'
    board[row][col] = figure
    return board


def play_game(board: list, moves: list) -> list:
    """
    Plays a sequence of moves on the board, ignoring invalid moves.

    Parameters:
    --------
    - board: list[list[str]]
        The initial state of the chessboard.
    - moves: list[str]
        A list of moves in string format.
        Each move is formatted as "square direction steps",
        e.g., "e2 U 2" moves the piece at 'e2' two steps up.

    Returns:
    --------
    - list[list[str]]:
        The resulting board after applying all valid moves.

    Notes:
    --------
    - Invalid moves are ignored; the board remains unchanged for those moves.
    - Does not enforce detailed chess rules (e.g., check, checkmate).

    Example:
    --------
    >>> board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],\
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', 'P'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    >>> moves = ['e2 U 2', 'e1 D 2', 'e7 D 2', 'e1 U 1', 'e8 D 1']
    >>> new_board = play_game(board, moves)
    >>> new_board[3][4]
    'P'
    >>> new_board[4][4]
    'p'
    >>> new_board[1][4]
    'K'
    >>> new_board[6][4]
    'k'
    """

    for move in moves:
        move = move.split()
        move[2] = int(move[2])
        new_board = make_move(board, tuple(move))
        if not new_board:
            continue
        board = new_board

    return board


def save_board(board: list, filename: str) -> None:
    """
    Saves the board to a file in the same format used by `read_board`.

    Parameters:
    --------
    - board: list[list[str]]
        The chessboard to save.
    - filename: str
        The path to the file where the board will be saved.

    Returns:
    --------
    - None

    Notes:
    --------
    - The board is written from top (rank 8) to bottom (rank 1).
    - Each row is written as a string of 8 characters.

    Example:
    --------
    >>> board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],\
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', 'P'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['.', '.', '.', '.', '.', '.', '.', '.'],\
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    >>> moves = ['e2 U 2', 'e7 D 2', 'e1 U 1', 'e8 D 1']
    >>> new_board = play_game(board, moves)
    >>> save_board(new_board, 'result.txt')
    >>> with open('result.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    rnbq.bnr
    ppppkppp
    ........
    ....p...
    ....P..P
    ........
    PPPPKPP.
    RNBQ.BNR
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join([''.join(row) for row in board[::-1]]))


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
