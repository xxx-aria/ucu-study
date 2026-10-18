"""My lab"""


def find_path(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    """
    Finds the path in coordinates according to treasure_map
    assuming that start is in (0, 0).
    If we go left by 1 from the start, the coordinate is (0, -1).
    If right – (0, 1).
    If we go up by 1 from the start, the coordinate is (-1, 0).
    If down – (1, 0).
    Return the list of coordinates.

    >>> find_path([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    [(0, 0), (-1, 0), (-2, 0), (-2, 1), (-2, 2), \
(-1, 2), (0, 2), (0, 3), (0, 4), (-1, 4), (-2, 4), \
(-3, 4), (-4, 4), (-4, 3), (-4, 2), (-4, 1), (-4, 0), \
(-4, -1), (-4, -2), (-4, -3), (-4, -4), (-4, -5), \
(-4, -6), (-4, -7), (-3, -7), (-2, -7), (-1, -7), \
(0, -7), (1, -7), (2, -7), (3, -7), (3, -6), \
(3, -5), (3, -4), (3, -3), (3, -2), (3, -1), \
(3, 0), (2, 0), (1, 0), (0, 0)]
    """

    path = [(0, 0)]
    for step in treasure_map:
        match step[0]:
            case 'U':
                path.extend([(path[-1][0] - i, path[-1][1]) for i in range(1, step[1] + 1)])
            case 'D':
                path.extend([(path[-1][0] + i, path[-1][1]) for i in range(1, step[1] + 1)])
            case 'R':
                path.extend([(path[-1][0], path[-1][1] + i) for i in range(1, step[1] + 1)])
            case 'L':
                path.extend([(path[-1][0], path[-1][1] - i) for i in range(1, step[1] + 1)])

    return path


def find_positive_path(path: list[tuple[int, int]]) -> list[tuple[int, int]]:
    '''Find the path with nonnegative coordinates by shifting
    the path horizontally and vertically by minimal steps.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> find_positive_path(path)
    [(4, 7), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), \
(4, 9), (4, 10), (4, 11), (3, 11), (2, 11), (1, 11), \
(0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (0, 5), \
(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), \
(3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), \
(7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (6, 7), (5, 7), (4, 7)]
    '''

    min_x_cor = 0
    min_y_cor = 0

    for coords in path:
        min_x_cor = min(min_x_cor, coords[0])
        min_y_cor = min(min_y_cor, coords[1])

    if min_x_cor == 0 and min_y_cor == 0:
        return path

    new_path = []
    for coords in path:
        new_path.append((coords[0] + abs(min_x_cor), coords[1] + abs(min_y_cor)))

    return new_path


def find_size(path: list[tuple[int, int]]) -> tuple[int, int]:
    '''Finds the size of the map: minimal number of points vertically
    and horizontally needed to build the path. Return tuple where the
    first coordinate is the height of the map and the second is the length.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_size(find_positive_path(find_path(treasure_map)))
    (8, 12)
    '''

    min_x_cor = float('inf')
    min_y_cor = float('inf')
    max_x_cor = float('-inf')
    max_y_cor = float('-inf')

    for coords in path:
        min_x_cor = min(min_x_cor, coords[0])
        min_y_cor = min(min_y_cor, coords[1])
        max_x_cor = max(max_x_cor, coords[0])
        max_y_cor = max(max_y_cor, coords[1])

    return (max_x_cor - min_x_cor + 1, max_y_cor - min_y_cor + 1)


def view_map(path: list[tuple[int, int]]) -> str:
    '''
    From path creates the map. Returns string representation of the map.
    If the coordinate is on the path, put the symbol 'x'.
    Otherwise use '.'.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> path = find_path(treasure_map)
    >>> view_map(path)
    'xxxxxxxxxxxx\\n\
x..........x\\n\
x......xxx.x\\n\
x......x.x.x\\n\
x......x.xxx\\n\
x......x....\\n\
x......x....\\n\
xxxxxxxx....'
    '''

    map_size = find_size(path)
    res_map = [['.'] * map_size[1] for _ in range(map_size[0])]
    for coords in find_positive_path(path):
        res_map[coords[0]][coords[1]] = 'x'

    res_map = [''.join(res_map[i]) for i in range(len(res_map))]
    return '\n'.join(res_map)


def find_vertices(treasure_map: list[tuple[str, int]]) -> list[tuple[int, int]]:
    '''Find the vertices of polygon that created on our map.

    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> find_vertices(treasure_map)
    [(-2, 0), (-2, 2), (0, 2), (0, 4), (-4, 4), (-4, -7), (3, -7), (3, 0)]
    >>> treasure_map = [('U', 2), ('R', 2), ('R', 2), ('D', 2), ('L', 4)]
    >>> find_vertices(treasure_map)
    [(0, 0), (-2, 0), (-2, 4), (0, 4)]
    '''

    directions = ''.join(
        [treasure_map[i][0] * treasure_map[i][1] for i in range(len(treasure_map))]
    )
    coords = find_path(treasure_map)[:-1]  # eliminating last (0, 0)

    vertices = []
    i = 0
    while i < len(coords):
        while i < len(coords) and directions[i] == directions[i - 1]:  # same direction
            i += 1
        if i == len(coords):
            break
        vertices.append(coords[i])
        i += 1

    return vertices


def calculate_polygon_area(vertices: list[tuple[int, int]]) -> int:
    '''
    Calculate the polygon area using the list of vertices of the
    polygon.
    >>> vertices = find_vertices([('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)])
    >>> calculate_polygon_area(vertices)
    61
    '''

    area = 0
    for i in range(-1, len(vertices) - 1):
        area += vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]

    return abs(area) // 2


def find_volume_treasure(area: int, length: int) -> int:
    '''
    Find the number of interior points. Each point is one treasure.
    >>> treasure_map = [('U', 2), ('R', 2), ('D', 2), ('R', 2), ('U', 4),\
 ('L', 11), ('D', 7), ('R', 7), ('U', 3)]
    >>> vertices = find_vertices(treasure_map)
    >>> area = calculate_polygon_area(vertices)
    >>> length = len(find_path(treasure_map))-1
    >>> find_volume_treasure(area, length)
    42
    '''

    return area - length // 2 + 1


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
