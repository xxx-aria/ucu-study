"""Renaming (Midterm 2023)"""


def read_file(filename: str) -> dict[tuple[str, str, str], str]:
    """Read file.

    >>> to_rename = read_file('renamed_locations_24.txt')
    >>> to_rename[('Донецька область', '', 'Краснолиманський район')] == 'Лиманський район'
    True
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('1. Перейменувати такі населені пункти та райони:'):
                break
        to_rename = {}
        region_name = ''
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(
                '2. Ця Постанова набирає чинності з дня, наступного за днем її опублікування.'
            ):
                break

            if line.split()[0][:-1].isdigit():
                region_name = line.split()[-2][:-2] + 'а область'
                continue
            line = line.replace('селище міського типу ', 'смт ')
            line = line.replace('селище ', 'с-ще ')
            line = line.replace('село ', 'с.')
            line = line.replace('місто ', 'м.')
            area_and_old, new_name = line[:-1].split(' на ')
            area_and_old = area_and_old.split()
            area_name = ''
            for i, w in enumerate(area_and_old):
                if w == 'району':
                    area_name = area_and_old[i - 1][:-3] + 'ий район'
                    area_and_old = area_and_old[: i - 1]
            if not area_name:
                for i, w in enumerate(area_and_old):
                    if w == 'ради':
                        area_name = area_and_old[i - 2][:-2] + 'а міська рада'
                        area_and_old = area_and_old[: i - 2]
            old_name = ' '.join(area_and_old)
            to_rename[(region_name, area_name, old_name)] = new_name
    return to_rename


def write_csv_file(info: dict[tuple[str, str, str], str], filename: str) -> None:
    """Write csv file.

    >>> write_csv_file(read_file('renamed_locations_24.txt'), 'output.csv')
    >>> with open('output.csv', encoding='utf-8') as f:
    ...     print(f.readline(), end='')
    ...     print(f.readline(), end='')
    regionname,areaname,oldname,newname
    Вінницька область,Барський район,с.Червоне,с.Грабівці"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('regionname,areaname,oldname,newname\n')
        for k, new_name in info.items():
            f.write(','.join(k + (new_name,)) + '\n')


if __name__ == '__main__':
    write_csv_file(read_file('renamed_locations_24.txt'), 'output.csv')
    import doctest

    print(doctest.testmod())
