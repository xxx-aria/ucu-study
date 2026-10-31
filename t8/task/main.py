def read_file(path):
    """
    Docstring for read_file

    :param path: Description
    :type path: str

    >>> read_file('example.txt')
    {'♥': [(0, 0), (1, 1), (2, 2)], '%': [(0, 1), (0, 2), (1, 2)]}
    """

    symbols = {}
    with open(path, 'r', encoding='utf-8') as f:
        while l := f.readline():
            l = l.strip()
            coords = f.readline().strip().split()
            symbols[l] = [(int(pos.split('_')[0]), int(pos.split('_')[1])) for pos in coords]
    return symbols


def save_pict_to_file(symbols, textfile):
    """
    Docstring for save_pict_to_file

    :param symbols: Description
    :param textfile: Description
    """

    x_max = float('-inf')
    y_max = float('-inf')
    for s, coords in symbols.items():
        for x, y in coords:
            x_max = max(x_max, x + 1)
            y_max = max(y_max, y + 1)

    picture = [[''] * x_max for _ in range(y_max)]

    for s, coords in symbols.items():
        for x, y in coords:
            picture[y][x] = s

    text = '\n'.join([' '.join(row) for row in picture])
    with open(textfile, 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())

    symbols = read_file('picture.txt')
    save_pict_to_file(symbols, 'picture_img.txt')
