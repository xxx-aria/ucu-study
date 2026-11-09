"""Pirates treasure"""


def define_direction(previous_direction: str, azimuth: int) -> str:
    """
    Calculate the new path direction based on the current direction
    and the pirate's biased azimuth. The azimuth is given in degrees
    and can be any non-negative multiple of 90. The directions are
    represented as 'N' for North, 'E' for East, 'S' for South, and 'W'
    for West.

    Args:
    previous_direction (str): The current direction ('N', 'E', 'S', 'W').
    azimuth (int): The azimuth in degrees (non-negative multiple of 90).

    Returns:
    str: The new direction as a single character string.

    For example:
    - If the current direction is North ('N') and the azimuth is 90 degrees,
      the new direction will be East ('E').
    - If the current direction is South ('S') and the azimuth is 90 degrees,
      the new direction will be West ('W').

    >>> define_direction('N', 0)
    'N'
    >>> define_direction('N', 90)
    'E'
    >>> define_direction('N', 180)
    'S'
    >>> define_direction('N', 270)
    'W'
    >>> define_direction('E', 90)
    'S'
    >>> define_direction('W', 270)
    'S'
    """
    directions = ('N', 'E', 'S', 'W')
    angle_change = azimuth % 360
    new_idx = (directions.index(previous_direction) + angle_change // 90) % 4
    return directions[new_idx]


def read_map(file_name: str) -> tuple[tuple[int, int], list[tuple[str, int]]]:
    """
    Reads a map from the specified file and interprets the directions
    and steps for navigation. The map file contains information about
    the starting coordinates and the steps to be taken in a specified
    direction. The initial direction is assumed to be North.

    The map file should be structured in such a way that it lists the
    starting coordinates (x, y) followed by directions (N, E, S, W)
    and the corresponding number of steps to take in each direction.

    Note: The file may contain empty lines, which should be ignored.

    Args:
    file_name (str): The pathname of the file containing the map data.

    Returns:
    tuple: A tuple containing two elements:
        - The first element is a tuple (x, y) representing the starting
          coordinates.
        - The second element is a list of tuples, where each tuple contains:
            - A direction (str): 'N' for North, 'E' for East, 'S' for South,
              or 'W' for West.
            - The number of steps (int) to take in that direction.

    >>> read_map("treasure_3.txt")
    ((0, 11), \
[('W', 5), ('W', 6), ('S', 7), ('E', 3), ('E', 4), \
('N', 5), ('E', 2), ('S', 2), ('E', 2), ('N', 4)])
    """
    starting_coords = None
    treasure_map = []

    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            coords = [int(num) for num in line.split()]
            if not starting_coords:
                starting_coords = tuple(coords)
                continue
            prev_direction = 'N'
            if len(treasure_map) > 0:
                prev_direction = treasure_map[-1][0]
            treasure_map.append((define_direction(prev_direction, coords[0]), coords[1]))
    return (starting_coords, treasure_map)


def find_path(
    start: tuple[int, int], treasure_directions: list[tuple[str, int]]
) -> list[tuple[int, int]]:
    """
    Calculates the path of coordinates based on the given start position
    and a series of directional steps. The start position is provided as
    a tuple of coordinates (x, y).

    The function interprets movement based on the following directional
    rules, with steps determining how far to move in a given direction:
    - 'W' (West): decreases the y-coordinate (moves left).
    - 'E' (East): increases the y-coordinate (moves right).
    - 'N' (North): decreases the x-coordinate (moves up).
    - 'S' (South): increases the x-coordinate (moves down).

    Args:
    start (tuple): A tuple representing the starting coordinates (x, y).
    treasure_directions (list of tuple): A list of tuples where each tuple
                                         contains:
                                         - A direction ('N', 'E', 'W', 'S')
                                         - An integer representing the number
                                           of steps to take in that direction.

    Returns:
    list of tuple: A list of coordinates (x, y) representing the path taken
                   from the start position, including all intermediate steps.

    >>> start = (0, 0)
    >>> path = [('E', 3), ('S', 3), ('W', 3), ('N', 3)]
    >>> find_path(start, path)
    [(0, 0), \
(0, 1), (0, 2), (0, 3), \
(1, 3), (2, 3), (3, 3), \
(3, 2), (3, 1), (3, 0), \
(2, 0), (1, 0), (0, 0)\
]
    """
    path = [start]
    for direction, steps in treasure_directions:
        if direction == 'N':
            for _ in range(steps):
                path.append((path[-1][0] - 1, path[-1][1]))
        if direction == 'E':
            for _ in range(steps):
                path.append((path[-1][0], path[-1][1] + 1))
        if direction == 'S':
            for _ in range(steps):
                path.append((path[-1][0] + 1, path[-1][1]))
        if direction == 'W':
            for _ in range(steps):
                path.append((path[-1][0], path[-1][1] - 1))
    return path


def find_treasure(
    path1: list[tuple[int, int]], path2: list[tuple[int, int]]
) -> tuple[int, int] | None:
    """
    Determines the location of the treasure based on the intersection of
    two paths. The function identifies the point of intersection and
    calculates the treasure's location based on the following conditions:

    - If the paths intersect at exactly one point, that point is the
      treasure's location.
    - If the paths intersect at exactly two points, the treasure is located
      at the midpoint between these two points. If the coordinates of the
      midpoint are fractional, they are rounded down to the nearest integer.
    - If the paths intersect at more than two points, it is impossible
      to determine the treasure's exact location, and the function
      returns `None`.

    Args:
    path1 (list of tuple): The first path, represented as
                           a list of coordinates (x, y).
    path2 (list of tuple): The second path, represented as
                           a list of coordinates (x, y).

    Returns:
    tuple or None: The coordinates (x, y) of the treasure if it
    can be determined, or `None`  if the treasure's location
    cannot be identified.

    >>> path1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
    >>> path2 = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> path3 = [(1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4)]
    >>> find_treasure(path1, path2)
    (2, 2)
    >>> find_treasure(path1, path3)
    (1, 2)
    >>> find_treasure(path2, path3)
    """
    in_common = set()
    for coords in path1:
        if coords in path2:
            in_common.add(coords)

    in_common = list(in_common)
    if len(in_common) == 1:
        return in_common[0]
    if len(in_common) == 2:
        return ((in_common[0][0] + in_common[1][0]) // 2, (in_common[0][1] + in_common[1][1]) // 2)
    return None


def find_size(path: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Calculates the size of the map based on the given path. The size of the map
    is determined by the minimal number of points needed vertically and
    horizontally to encompass the entire path. The height is the difference
    between the maximum and minimum x-coordinates, and the width is the
    difference between the maximum and minimum y-coordinates.

    Args:
    path (list of tuple): A list of coordinates (x, y) representing the path.

    Returns:
    tuple: A tuple (height, width) where:
        - height is the number of points needed vertically.
        - width is the number of points needed horizontally.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> find_size(path)
    (3, 3)
    """
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')

    for x, y in path:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    return (abs(x_max - x_min + 1), abs(y_max - y_min + 1))


def shift_path(path: list[tuple[int, int]]) -> tuple[tuple[int, int], list[tuple[int, int]]]:
    """
    Shifts the given path to ensure that all coordinates are non-negative
    and the smallest coordinate is positioned at (0, 0).

    The function returns a tuple, where the first element is a tuple
    containing the minimum y and x values before the shift, and the second
    element is the list of shifted coordinates.

    Args:
    path (list of tuple): A list of tuples where each tuple represents a
                          coordinate (x, y) along the path.

    Returns:
    tuple: A tuple where:
        - The first element is a tuple representing the minimum
          y-coordinate and x-coordinate found in the path.
        - The second element is a list of tuples representing the shifted path,
          where all coordinates are non-negative.

    >>> path = [(2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> shift_path(path)
    ((2, 2), [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    """
    x_min = float('inf')
    y_min = float('inf')

    for x, y in path:
        x_min = min(x_min, x)
        y_min = min(y_min, y)

    new_path = [(x - x_min, y - y_min) for x, y in path]
    return ((x_min, y_min), new_path)


def decode_map(file_name1: str, file_name2: str, map_file_name: str) -> None:
    """
    Draws a map that visualizes two paths and the treasure (if it exists)
    based on the paths provided in two input files. The map is written
    to the specified output file.

    - The paths are marked with `.`.
    - The start of the first path is marked with `1`.
    - The start of the second path is marked with `2`.
    - If the start of the first and second path coincides, it is
      marked with `3`.
    - If the treasure is found (i.e., the paths intersect at a specific point),
      it is marked with `x`. The treasure marker `x` overwrites the start
      markers '1' and '2' if they coincide with the treasure's location.

    Args:
    file_name1 (str): The name of the file containing the first path.
    file_name2 (str): The name of the file containing the second path.
    map_file_name (str): The name of the output file where the map will be drawn.

    Returns:
    None: The map is written directly to the output file.

    >>> decode_map('treasure_1.txt', 'treasure_2.txt', 'output.txt')
    >>> with open('output.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    1..
    . .
    ..x.2
      . .
      ...
    """
    path_1 = find_path(*read_map(file_name1))
    path_2 = find_path(*read_map(file_name2))

    pathes = shift_path(path_1 + path_2)[1]
    path_1, path_2 = pathes[: len(path_1)], pathes[len(path_1) :]

    map_size = find_size(pathes)

    map_res = [[' '] * map_size[1] for _ in range(map_size[0])]

    for x, y in pathes:
        map_res[x][y] = '.'

    map_res[path_1[0][0]][path_1[0][1]] = '1'
    map_res[path_2[0][0]][path_2[0][1]] = '2'
    if path_1[0] == path_2[0]:
        map_res[path_1[0][0]][path_1[0][1]] = '3'

    treasure_coords = find_treasure(path_1, path_2)
    if treasure_coords:
        map_res[treasure_coords[0]][treasure_coords[1]] = 'x'

    with open(map_file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join([''.join(row).rstrip() for row in map_res]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
