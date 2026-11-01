""" "Zerno"""


def read_file(filepath: str) -> tuple[int, int, list[list]]:
    """
    Read grain storage parameters and loading requests from file.

    Args:
        filepath: Path to input file containing storage configuration

    Returns:
        tuple: (num_storages, storage_capacity_kg, requests)
        where requests is a list of [grain_type, mass_kg] pairs

    File format:
        Line 1: "Зерносховищ: N" - number of storages
        Line 2: "Місткість: M" - capacity in kg
        Line 3+: "id,grain_type,mass" - loading requests

    Example:
        >>> read_file("input.txt")
        (2, 3000, [['Сотниця', 2000], ['Фортеця', 520], ['Сотниця', 1250]])
    """
    storages = []
    with open(filepath, 'r', encoding='utf-8') as f:
        num = f.readline().strip().split()[-1]
        capacity = f.readline().strip().split()[-1]
        for line in f:
            _, grain_type, mass = line.strip().split(',')
            storages.append([grain_type, int(mass)])
    return int(num), int(capacity), storages


def load_grain(
    storage_grain_type: str | None,
    storage_free_capacity: int,
    request_grain_type: str,
    request_capacity: int,
) -> tuple[str, str | None, int]:
    """
    Attempt to load grain into a single storage.

    Args:
        storage_grain_type: Current grain type in storage (None if empty)
        storage_free_capacity: Available capacity in storage (kg)
        request_grain_type: Type of grain to load
        request_capacity: Amount of grain to load (kg)

    Returns:
        tuple: (status, grain_type, free_capacity)
        - status: 'accepted' if loaded successfully, 'denied' otherwise
        - grain_type: Updated grain type in storage
        - free_capacity: Remaining free capacity after operation

    Rules:
        - Can only load if storage is empty (None) or has same grain type
        - Can only load if there is enough free capacity

    Examples:
        >>> load_grain(None, 3000, 'Сотниця', 2000)
        ('accepted', 'Сотниця', 1000)
        >>> load_grain('Сотниця', 1000, 'Фортеця', 520)
        ('denied', 'Сотниця', 1000)
        >>> load_grain('Сотниця', 1000, 'Сотниця', 500)
        ('accepted', 'Сотниця', 500)
    """
    if storage_grain_type and storage_grain_type != request_grain_type:
        return ('denied', storage_grain_type, storage_free_capacity)
    if storage_free_capacity < request_capacity:
        return ('denied', storage_grain_type, storage_free_capacity)

    return ('accepted', request_grain_type, storage_free_capacity - request_capacity)


def distribute_grain(
    num_storages: int, storage_capacity: int, requests: list[list]
) -> list[tuple[str, list[tuple]]]:
    """
    Distribute grain among storages processing requests sequentially.

    Args:
        num_storages: Number of available storages
        storage_capacity: Maximum capacity of each storage (kg)
        requests: List of [grain_type, mass_kg] pairs to process

    Returns:
        List of tuples: (status, storages_state) for each request
        - status: 'accepted' or 'denied'
        - storages_state: List of (grain_type, loaded_mass) tuples for each storage

    Processing rules:
        - Requests are processed in order
        - For each request, check storages from first to last
        - Load into first storage that matches grain type (or is empty) and has capacity
        - If no suitable storage found, deny the request

    Example:
        >>> num_storages, storage_capacity, requests = (2, 3000, [['Сотниця', 2000],\
 ['Фортеця', 520], ['Сотниця', 1250]])
        >>> distribute_grain(num_storages, storage_capacity, requests)
        [('accepted', [('Сотниця', 2000), (None, 0)]), ('accepted', [('Сотниця', 2000),\
 ('Фортеця', 520)]), ('denied', [('Сотниця', 2000), ('Фортеця', 520)])]
    """
    res = []
    storages = [(None, 0)] * num_storages
    for req in requests:
        for i, (grain, capacity) in enumerate(storages):
            status, grain_type, _ = load_grain(grain, storage_capacity - capacity, req[0], req[1])
            if status == 'accepted':
                storages[i] = (grain_type, capacity + req[1])
                res.append((status, storages.copy()))
                break
        if status == 'denied':
            res.append((status, storages.copy()))
    return res


def write_report(report_by_requests: list[tuple], filepath: str) -> None:
    """
    Write distribution report to output file.

    Args:
        report_by_requests: List of (status, storages) tuples from distribute_grain
        filepath: Path to output file

    Output format:
        For each request:
            Запит N: [Прийнято/Відхилено]
            Сховище 1: Заповнення: Xкг, Сорт: [grain_type]
            Сховище 2: Заповнення: Yкг, Сорт: [grain_type]
            ...

    Example:
        >>> import tempfile
        >>> report = [('accepted', [('Сотниця', 2000), (None, 0)]),
        ...           ('accepted', [('Сотниця', 2000), ('Фортеця', 520)]),
        ...           ('denied', [('Сотниця', 2000), ('Фортеця', 520)])]
        >>> with tempfile.NamedTemporaryFile(mode='r+', delete=False) as f:
        ...     write_report(report, f.name)
        ...     print(f.read().strip())
        Запит 1: Прийнято
        Сховище 1: Заповнення: 2000кг, Сорт: Сотниця
        Сховище 2: Заповнення: 0кг, Сорт: None
        Запит 2: Прийнято
        Сховище 1: Заповнення: 2000кг, Сорт: Сотниця
        Сховище 2: Заповнення: 520кг, Сорт: Фортеця
        Запит 3: Відхилено
        Сховище 1: Заповнення: 2000кг, Сорт: Сотниця
        Сховище 2: Заповнення: 520кг, Сорт: Фортеця
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for i, req in enumerate(report_by_requests):
            status, storages = req
            f.write(f'Запит {i+1}: {'Прийнято' if status == 'accepted' else 'Відхилено'}\n')
            for j, storage in enumerate(storages):
                f.write(f'Сховище {j+1}: Заповнення: {storage[1]}кг, Сорт: {storage[0]}\n')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    # write_report(distribute_grain(*read_file("input.txt")), 'output.txt')
