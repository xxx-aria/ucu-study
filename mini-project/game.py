"""root@nowhere"""

import random
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
PURPLE = '\033[35m'
GRAY = '\033[90m'
BOLD = '\033[1m'
RESET = '\033[0m'

UNLOCK_TRIES = 3

WRONG_COMMAND = f'{YELLOW}[?] Невідома команда.{RESET}'
EXIT_MESSAGE = '[EXIT] Дякую за гру!'

COMMANDS_HELP = {
    'help': 'Перелік і пояснення усіх доступних команд',
    'notes': 'Переглянути твої зібрані фрагменти',
    'exit': 'Закінчити гру',
    'cd назва-папки': 'Перейти в папку',
    'cd ..': 'Перейти назад в минулу папку',
    'ls': 'Файли і папки, які є у поточній папці',
    'cat назва-файлу': 'Прочитати вміст файлу .txt',
    'decrypt notes ключ': 'Розшифрувати пароль; лише при повному notes',
    'unlock пароль': f'Відкрити сховище ({UNLOCK_TRIES} спроби)',
    'play назва-файлу': 'Зіграти гру - лише для файлів .game',
}


MAX_TRACE_LVL = 100
TRACE_ADD = {'cat': 3, 'cd': 1, 'notes': 1, 'play': 5}

FOUND_TEXT = '[+] Знайдено фрагмент #'
FOUND_KEY = '[+] Знайдено ключ - '

FILE_SYSTEM = {
    'admin': {
        'type': 'dir',
        'content': {
            'net.game': {'type': 'game'},
            'fw.game': {'type': 'game'},
            'port.game': {'type': 'game'},
            'ids.game': {'type': 'game'},
        },
    },
    'sysadmin': {
        'type': 'dir',
        'content': {
            'backup': {
                'type': 'dir',
                'content': {
                    'my_first_day_at_work.txt': {'type': 'file', 'content': None},
                    'server_news.txt': {'type': 'file', 'content': None},
                },
            },
            'diary': {
                'type': 'dir',
                'content': {'key_info.txt': {'type': 'file', 'content': None}},
            },
        },
    },
    'analyst': {
        'type': 'dir',
        'content': {
            'nothing_interesting.txt': {'type': 'file', 'content': None},
            'top-secret': {
                'type': 'dir',
                'content': {'ALL_I_FOUND.txt': {'type': 'file', 'content': None}},
            },
        },
    },
    'mail': {
        'type': 'dir',
        'content': {
            'old_jokes.txt': {'type': 'file', 'content': None},
            'fantasy_football.txt': {'type': 'file', 'content': None},
            'inbox': {
                'type': 'dir',
                'content': {
                    'vacation_plans.txt': {'type': 'file', 'content': None},
                    'my_lunch.txt': {'type': 'file', 'content': None},
                    'shopping_list.txt': {'type': 'file', 'content': None},
                    'from_engineer.txt': {'type': 'file', 'content': None},
                    'final_warning.txt': {'type': 'file', 'content': None},
                    'fantasy_football.txt': {'type': 'file', 'content': None},
                    'office_plants.txt': {'type': 'file', 'content': None},
                },
            },
            'sent': {
                'type': 'dir',
                'content': {
                    'cat_names_list.txt': {'type': 'file', 'content': None},
                    'to_engineer.txt': {'type': 'file', 'content': None},
                    'birthday_wishlist.txt': {'type': 'file', 'content': None},
                    'recipe_borsch.txt': {'type': 'file', 'content': None},
                    'server_migration.txt': {'type': 'file', 'content': None},
                    'best_films.txt': {'type': 'file', 'content': None},
                },
            },
        },
    },
    'readme.txt': {'type': 'file', 'content': None},
}

GAMES_DESCR = {
    'net.game': f'{CYAN}[NET]{RESET} Десь у мережі 5×5 прихований канал \
зв\'язку - 3 клітинки поруч.\n\
Вводь координати (напр. B3), щоб просканувати сектор.\n\
[крапка = порожньо (мимо), X = сигнал]\n\
Напишіть q, щоб вийти з мінігри.',
    'fw.game': f'{CYAN}[FW]{RESET} Фаєрвол тримає 5 вузлів, \
тобі потрібно вимкнути всі вузли (○ ○ ○ ○ ○).\n\
[{RED}●{RESET} - активний, {GREEN}○{RESET} - вимкнений]\n\
Введи номер вузла [1–5], щоб перемкнути його і сусідні вузли.\n\
Увага! Сусідні вузли також перемикаються. Тобто за один хід перемикається 2 або 3 вузли.\n\
Напишіть q, щоб вийти з мінігри.',
    'port.game': f'{CYAN}[PORT]{RESET} Один порт від 1000 до 9999 відкритий.\n\
Введи номер порту - система підкаже "вище" чи "нижче" тобі потрібно змінити здогадку.\n\
Напишіть q, щоб вийти з мінігри.',
    'ids.game': f'{CYAN}[IDS]{RESET} Система перевіряє, чи ти бот.\n\
 На екрані з\'явиться код - введи його ТОЧНО і швидко (до 5 секунд). Потрібно 3 успіхи загалом.\n\
Напишіть q, щоб вийти з мінігри.',
}


def setup_diary_pass() -> None:
    """Генерує випадковий пароль до щоденника й записує його у файлову систему."""
    diary_pass = random.choice(['qwerty', 'abc', 'cool', 'wow', 'nowhere']) + str(
        random.randint(100, 999)
    )
    FILE_SYSTEM['sysadmin']['content']['diary']['password'] = diary_pass
    secret_dir = FILE_SYSTEM['analyst']['content']['top-secret']['content']
    secret_dir['ALL_I_FOUND.txt']['content'] = f'Я впевнений, що у щоденнику (diary) \
нашого сисадміна знаходиться дещо цікаве...\nЗміг дізнатись пароль: {diary_pass}'


def get_fragments_locations(answer: str) -> dict[str, tuple[str, int]]:
    """Випадково розкладає зашифровані символи пароля по файлах і міні іграх."""
    locations = [
        random.choice(
            [
                'from_engineer.txt',
                'to_engineer.txt',
                'server_migration.txt',
                'final_warning.txt',
                'server_news.txt',
            ]
        ),
        'net.game',
        'fw.game',
        'port.game',
        'ids.game',
    ]
    random.shuffle(locations)

    fragments_locs = {}
    for i, loc in enumerate(locations):
        fragments_locs[loc] = (answer[i], i)

    return fragments_locs


def unlock_diary(diary_pass: str) -> bool | None:
    """Просить пароль до щоденника.

    Повертає True, якщо правильний, False - ні або q, None - exit.
    """
    print(f'{YELLOW}[!] Папку diary захищено особистим паролем сисадміна. \
Можливо, варто перевірити листування або папку підозрілого аналітика...{RESET}')
    print('Введіть пароль або q, щоб вийти.')
    guess = input('>>> ').strip()
    if guess == 'exit':
        return None
    if guess.lower() == 'q':
        return False
    if guess != diary_pass:
        print(f'{RED}[X] Неправильний пароль.{RESET}')
        return False
    print(f'{GREEN}[+] Пароль прийнято.{RESET}')
    return True


# ================= admin, міні ігри


def guess_admin_pin() -> bool | None:
    """Мінігра на вгадування PIN-коду з підказками.

    True - вгадано, False - q, None - exit.
    """
    print(f'{YELLOW}[!] Папку admin захищено особистим PIN-кодом.{RESET}')
    pin = str(random.randint(100, 999))
    print('PIN-код складається з 3 цифр.')
    print('Кількість спроб необмежена. Напишіть q, щоб припинити вгадування.')
    while (guess := input('>>> ').strip()) != pin:
        if guess == 'exit':
            return None
        if guess.lower() == 'q':
            return False
        if len(guess) != 3 or not guess.isdigit():
            print('Неправильний формат.')
            continue

        if guess == pin:
            break

        are_present = 0
        at_pos = 0
        for i in range(3):
            if guess[i] in pin and guess[: i + 1].count(guess[i]) <= pin.count(guess[i]):
                are_present += 1
            if guess[i] == pin[i]:
                at_pos += 1

        print('Невдала спроба.')
        print(f'Цифр, які є у PIN-коді: {are_present}')
        print(f'Цифр на своїх позиціях: {at_pos}')
    print(f'{GREEN}[+] PIN прийнято. Доступ відкрито.{RESET}')
    return True


def get_connection_matrix(n: int) -> list[list[int]]:
    """Створює сітку n x n з випадковим каналом зв'язку з 3 клітинок."""
    connection_matrix = [[0] * n for _ in range(n)]
    conn_i, conn_j = random.randint(0, n - 1), random.randint(0, n - 1)
    connection_matrix[conn_i][conn_j] = 1
    for _ in range(2):
        while True:
            add_i, add_j = random.choice([(1, 0), (-1, 0), (0, -1), (0, 1)])
            next_conn_i = conn_i + add_i
            next_conn_j = conn_j + add_j
            if not 0 <= next_conn_i < n or not 0 <= next_conn_j < n:
                continue
            if connection_matrix[next_conn_i][next_conn_j]:
                continue
            conn_i = next_conn_i
            conn_j = next_conn_j
            break
        connection_matrix[conn_i][conn_j] = 1
    return connection_matrix


def print_connection_matrix(connection_matrix: list[list[int]]) -> None:
    """Виводить сітку з уже просканованими секторами."""
    n = len(connection_matrix)
    print('   ' + '   '.join([chr(o) for o in range(ord('A'), ord('A') + n)]))
    print(' +' + '---+' * n)
    for i, row in enumerate(connection_matrix):
        row = ['X' if x == 1 else '.' if x == -1 else ' ' for x in row]
        print(str(i + 1) + '| ' + ' | '.join(row) + ' |')
        print(' +' + '---+' * n)


def sea_battle() -> bool | None:
    """Мінігра морський бій: знайти 3 клітинки каналу.

    True - перемога, False - q, None - exit.
    """
    connection_matrix = get_connection_matrix(5)
    user_matrix = [[0] * 5 for _ in range(5)]
    left = 3
    while left > 0:
        print_connection_matrix(user_matrix)
        print('Введи координату для пострілу (напр. C4).')
        user_coord = input('>>> ').strip()
        if user_coord == 'exit':
            return None
        if user_coord == 'q':
            return False
        if len(user_coord) != 2:
            print('Неправильна координата.')
            continue
        if not user_coord[0].isalpha() or user_coord[1] not in '12345':
            print('Неправильна координата.')
            continue
        user_coord = user_coord.upper()
        num_i = int(user_coord[1]) - 1
        letter_j = ord(user_coord[0]) - ord('A')
        if not 0 <= num_i < 5 or not 0 <= letter_j < 5:
            print('Неправильна координата.')
            continue
        if user_matrix[num_i][letter_j]:
            print(f'{user_coord}: вже проскановано.')
            continue

        if connection_matrix[num_i][letter_j] and not user_matrix[num_i][letter_j]:
            left -= 1
            print(f'{user_coord}: сигнал виявлено! {3 - left}/3.')
            user_matrix[num_i][letter_j] = 1
        elif not connection_matrix[num_i][letter_j]:
            print(f'{user_coord}: тиша.')
            user_matrix[num_i][letter_j] = -1

    print_connection_matrix(user_matrix)
    return True


def do_switch(seq: list[bool], i: int) -> None:
    """Перемикає вузол i його сусідів."""
    seq[i] = not seq[i]
    if i < 4:
        seq[i + 1] = not seq[i + 1]
    if i > 0:
        seq[i - 1] = not seq[i - 1]


def get_random_seq() -> list[bool] | None:
    """Створює випадковий стан фаєрвола.

    None, якщо вийшов уже вимкнений (потрібно переробити).
    """
    seq = [True] * 5
    for i in range(random.randint(1, 5)):
        i = random.randint(0, 4)
        do_switch(seq, i)
    if seq == [True] * 5:
        return None
    return seq


def turn_off_firewall() -> bool | None:
    """Мінігра, де потрібно вимкнути всі вузли.

    True - перемога, False - q, None - exit.
    """
    circle = GREEN + "○" + RESET
    full_circle = RED + "●" + RESET
    while not (seq := get_random_seq()):
        continue
    while seq != [True] * 5:
        print(''.join([circle if x else full_circle for x in seq]))
        print('Введіть номер лампочки, яку перемкнути [1 - 5].')
        user_inp = input('>>> ').strip()
        if user_inp == 'exit':
            return None
        if user_inp == 'q':
            return False
        try:
            idx = int(user_inp)
        except ValueError:
            print('Неправильний номер.')
            continue
        if not 1 <= idx <= 5:
            print('Неправильний номер.')
            continue
        do_switch(seq, idx - 1)
    return True


def find_port() -> bool | None:
    """Мінігра, в якій треба знайти порт за підказками вище/нижче.

    True - знайдено, False - q, None - exit.
    """
    port = random.randint(1000, 9999)
    while True:
        guess = input('>>> ').strip()
        if guess == 'exit':
            return None
        if guess == 'q':
            return False
        try:
            guess = int(guess)
        except ValueError:
            print('Неправильний порт.')
            continue
        if not 1000 <= guess <= 9999:
            print('Порт складається з 4 цифр.')
            continue
        if guess > port:
            print('Візьміть нижче.')
        elif guess < port:
            print('Візьміть вище.')
        else:
            print(f'Порт знайдено: {port}.')
            return True


def bypass_system() -> bool | None:
    """Мінігра, де треба здійснити обхід системи розпізнавання - тричі швидко ввести код.

    True - перемога, False - q, None - exit.
    """
    words = 3
    while words > 0:
        random_combo = ''
        for _ in range(5):
            random_combo += chr(random.randint(ord('A'), ord('z')))
        time.sleep(1)
        print(f'{3 - words}/3\t' + random_combo, flush=True)
        t1 = time.time()
        user_inp = input('>>> ')
        t2 = time.time()
        if user_inp == 'exit':
            return None
        if user_inp == 'q':
            return False
        if user_inp.strip() != random_combo:
            print('Неправильно.')
            continue
        if t2 - t1 > 5:
            print(f'Запізно: {t2-t1:.2f} с.')
            continue
        words -= 1
    return True


def do_play(
    file_name: str,
    fragments_locs: dict[str, tuple[str, int]],
    curr_loc: list[str],
    collected: set[str],
) -> tuple[str, int] | bool | None:
    """Запускає вибрану мінігру з папки admin.

    Повертає (символ, позиція) при перемозі, None - exit, False - інакше.
    """
    if curr_loc[-1] != 'admin' or file_name not in GAMES_DESCR:
        print(f'{RED}[X] Файл не знайдено.{RESET}')
        return False
    if file_name in collected:
        print(f'{RED}[X] Цю систему вже зламано.{RESET}')
        return False
    letter, idx = fragments_locs[file_name]
    print(GAMES_DESCR[file_name])
    res = False
    match file_name:
        case 'net.game':
            res = sea_battle()
        case 'fw.game':
            res = turn_off_firewall()
        case 'port.game':
            res = find_port()
        case 'ids.game':
            res = bypass_system()
    if res is None:
        return None
    if res:
        return letter, idx
    print(f'{GRAY}[Q] Ви вийшли з мінігри {file_name}.{RESET}')
    return False


# =================


def print_location(curr_loc: list[str], trace_lvl: int) -> None:
    """Виводить запрошення терміналу з поточним шляхом і відсотком (рівнем) трасування."""
    trace_color = GREEN
    if trace_lvl >= 80:
        trace_color = RED
    elif trace_lvl >= 50:
        trace_color = YELLOW
    print(
        '\n'
        + CYAN
        + 'root@nowhere:'
        + '/'.join(curr_loc)
        + '$'
        + RESET
        + trace_color
        + f' [TRACING {trace_lvl}%/{MAX_TRACE_LVL}%]'
        + RESET
    )


def get_answer(answers_file: str) -> str:
    """Читає слова з файлу й обирає випадковий пароль."""
    answers = []
    with open(answers_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line := line.strip():
                answers.append(line)
    answer = random.choice(answers)
    return answer


def get_encrypted_answer(answer: str, shift: int = 0) -> list[str]:
    """Шифрує пароль (зсуває кожен символ на shift)."""
    return [chr(ord(l) + shift) for l in answer]


def wait_enter(message: str) -> bool:
    """Чекає, поки гравець натисне Enter.

    False, якщо введено exit.
    """
    while user_inp := input('>>> ').strip():
        if user_inp == 'exit':
            return False
        print(message)
    return True


def print_intro() -> bool:
    """Виводить передісторію, мету, правила й завантаження системи.

    False, якщо введено exit.
    """
    print(
        f'Три тижні тому сервер компанії {CYAN}{BOLD}NOWHERE{RESET} зник з усіх мереж.', flush=True
    )
    time.sleep(2)
    print('Офіційно - його вимкнули.', flush=True)
    time.sleep(1.5)
    print('Неофіційно... ', end='', flush=True)
    time.sleep(2.5)
    print('він досі працює. ', end='', flush=True)
    time.sleep(1)
    print('І щось приховує.', flush=True)
    time.sleep(1)
    print(f'{YELLOW}Натисни Enter, щоб продовжити...{RESET}')
    if not wait_enter(f'{YELLOW}Натисни Enter, щоб продовжити...{RESET}'):
        return False

    print(
        '''Тобі вдалося зайти у систему. Ти - root.
Але адмін сховав найважливіше: сховище політичних таємниць.
Пароль він розбив на зашифровані фрагменти й розкидав по системі.

ТВОЯ МЕТА:
\tЗнайди всі фрагменти, розшифруй пароль
\tі відкрий сховище (лише 3 спроби).
ЯК ГРАТИ:
\t- Вводь команди, як у терміналі.
\t  Нові команди відкриватимуться поступово.
\t- Вийти з гри будь-коли - exit
ОБЕРЕЖНО:
\tКожна дія підвищує рівень ТРАСУВАННЯ.
\tЯкщо він дійде до 100% - тебе знайдуть.\n''',
        flush=True,
    )
    time.sleep(5)
    print(f'{YELLOW}Натисни Enter, щоб підключитися...{RESET}')
    if not wait_enter(f'{YELLOW}Натисни Enter, щоб підключитися...{RESET}'):
        return False
    print('SYSTEM BOOT SEQUENCE INITIATED.\nLaunching NOWHERE OS... ', end='', flush=True)
    time.sleep(1)
    print(f'{GREEN}[OK]{RESET}')
    print('Loading core modules... ', end='', flush=True)
    time.sleep(1)
    print(f'{GREEN}[OK]{RESET}')
    print('Checking hardware integrity... ', end='', flush=True)
    time.sleep(1)
    print(f'{GREEN}[OK]{RESET}')
    print('Establishing secure uplink... ', end='', flush=True)
    time.sleep(1)
    print(f'{GREEN}Connected.{RESET}')
    print('\nNOWHERE is fully operational. Welcome back, root.', flush=True)
    time.sleep(2)
    print(f'{RED}CRITICAL ERROR: Received foreign message [press Enter].{RESET}')
    if not wait_enter(f'{YELLOW}Натисни Enter, щоб прочитати повідомлення...{RESET}'):
        return False
    print(PURPLE + '''?: Привіт, root. Радий тебе знову бачити. Покладаюсь на тебе.
Щоб дізнатись про взаємодію з системою введи наступну команду:
\tcat readme.txt''' + RESET)
    return True


def add_command(curr_commands: list[str], command: str) -> None:
    """Відкриває гравцю нову команду й повідомляє про це."""
    command = command.strip().lower()
    if command not in COMMANDS_HELP:
        return
    curr_commands.append(command)
    print(f'{YELLOW}[НОВА КОМАНДА]{RESET} Перегляньте, як працює команда {command}, ввівши help.')


def print_help(available_commands: list[str]) -> None:
    """Виводить доступні команди з поясненнями."""
    for c in available_commands:
        print(f'\t{c:<25}- {COMMANDS_HELP[c]}')


def do_ls(current_loc: list[str]) -> list[str]:
    """Повертає список файлів і папок у поточній папці."""
    loc = FILE_SYSTEM
    for x in current_loc[2:]:
        loc = loc[x]['content']
    return list(loc)


def do_cat(comm: str, current_loc: list[str], files_contents_pathname: str) -> str | None:
    """Виводить вміст .txt файлу.

    Повертає назву файлу або None, якщо прочитати не вдалося.
    """
    file_name = comm.split()[1]
    if not file_name.endswith('.txt'):
        print(f'{RED}[X] Даний формат файлу не підтримується для читання{RESET}')
        return None
    if file_name not in do_ls(current_loc):
        print(f'{RED}[X] Файл не знайдено{RESET}')
        return None

    loc = FILE_SYSTEM
    for x in current_loc[2:]:
        loc = loc[x]['content']
    loc = loc[file_name]

    if loc.get('content', None):
        print(file_name)
        print(loc['content'])
        return file_name
    if len(current_loc) == 2 and file_name == 'readme.txt':
        print(FILE_SYSTEM['readme.txt']['content'])
        return file_name

    contents = ''
    with open(files_contents_pathname, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == file_name:
                print(file_name)
                while (file_line := f.readline()).strip():
                    contents += file_line
                    loc['content'] = contents
                print(contents)
                return file_name

    print(f'{RED}[X] Файл не знайдено{RESET}')
    return None


def do_cd(comm: str, location: list[str], unlocked_dirs: set[str]) -> list[str] | None:
    """Переходить у папку з перевіркою PIN чи пароля за потреби.

    Повертає новий шлях або None (якщо exit).
    """
    curr_loc = FILE_SYSTEM
    for x in location[2:]:
        curr_loc = curr_loc[x]['content']
    dest = comm.split()[1]
    if dest == '..':
        if len(location) > 2:
            location = location[:-1]
        return location
    if dest not in curr_loc:
        print(f'{RED}[X] Неправильна команда: папки {dest} не існує{RESET}')
        return location
    if curr_loc[dest]['type'] != 'dir':
        print(f'{RED}[X] Неправильна команда: {dest} не є папкою{RESET}')
        return location

    if dest in ('admin', 'diary') and dest not in unlocked_dirs:
        if dest == 'admin':
            res = guess_admin_pin()
        else:
            res = unlock_diary(curr_loc[dest]['password'])
        if res is None:
            return None
        if not res:
            print(f'{RED}[X] Невдала спроба розблокування папки {dest}{RESET}')
            return location
        unlocked_dirs.add(dest)
    return location + [dest]


def is_valid_command(user_comm: str, available_commands: list[str]) -> bool:
    """Перевіряє, чи команда доступна для використання."""
    if not user_comm.split():
        return False
    for comm in available_commands:
        if comm.split()[0] == user_comm.split()[0]:
            return len(comm.split()) == len(user_comm.split())
    return False


# =================


def do_decrypt(user_key: str, fragments: list[str], key_found: bool, key: int, answer: str) -> None:
    """Розшифровує й показує пароль, якщо зібрано всі символи та ключ правильний."""
    if '_' in fragments:
        print(f'{RED}[X] Неможливо розшифрувати пароль: нотатки неповні.{RESET}')
        return
    if not key_found:
        print(f'{RED}[X] Неможливо розшифрувати пароль: ключ ще не знайдений.{RESET}')
        return
    if user_key != str(key):
        print(f'{RED}[X] Неможливо розшифрувати пароль: неправильний ключ.{RESET}')
        return
    print('Дешифрування пароля', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.')
    print(f'{GREEN}{BOLD}[PASSWORD] ПАРОЛЬ ДО СИСТЕМИ: {answer}{RESET}')
    print('Скористайтеся командою unlock')


def play_game() -> None:
    """Головний цикл гри (вступ, обробка команд користувача, кінцівки)."""
    print(GREEN + '*' * 70)
    print(f'{'root@nowhere':^70}')
    print('*' * 70 + RESET)

    key = random.randint(1, 9)

    current_loc = ['', 'home']
    available_commands = ['cat readme.txt', 'exit']

    answer = get_answer('words.txt')
    answer_encrypted = get_encrypted_answer(answer, key)

    fragments = ['_'] * len(answer)
    fragments_locs = get_fragments_locations(answer_encrypted)

    setup_diary_pass()

    key_found = False
    trace_lvl = 0
    tries = 0
    unlocked_dirs = set()
    collected = set()

    if not print_intro():
        print(EXIT_MESSAGE)
        return

    print_location(current_loc, trace_lvl)
    while (user_comm := input('>>> ').strip()) != 'cat readme.txt':
        if user_comm == 'exit':
            print(EXIT_MESSAGE)
            return
        print(WRONG_COMMAND)
    available_commands.remove('cat readme.txt')

    with open('game_readme.txt', 'r', encoding='utf-8') as f:
        FILE_SYSTEM['readme.txt']['content'] = ''
        for line in f:
            print(line.strip('\n'))
            FILE_SYSTEM['readme.txt']['content'] += line

    add_command(available_commands, 'help')

    while (user_comm := input('>>> ').strip()) != 'help':
        if user_comm == 'exit':
            print(EXIT_MESSAGE)
            return
        print(WRONG_COMMAND)

    available_commands.extend(
        [
            'notes',
            'cd назва-папки',
            'cd ..',
            'ls',
            'cat назва-файлу',
            'decrypt notes ключ',
            'unlock пароль',
        ]
    )

    print_help(available_commands)
    print('Підказка: почни з команди ls, щоб розвідати цю папку.')

    exited = False
    while trace_lvl < MAX_TRACE_LVL and tries < UNLOCK_TRIES:

        print_location(current_loc, trace_lvl)
        user_comm = input('>>> ').strip()

        if not is_valid_command(user_comm, available_commands):
            print(WRONG_COMMAND)
            continue

        match user_comm:
            case 'help':
                print_help(available_commands)
                continue
            case 'exit':
                exited = True
                break
            case 'notes':
                print('Зібрані символи:')
                symbols = []
                for symbol in fragments:
                    if symbol == '_':
                        symbols.append(GRAY + symbol + RESET)
                    else:
                        symbols.append(PURPLE + symbol + RESET)
                print('\t' + ' '.join(symbols))
                print(f'Ключ: {key if key_found else 'ще не знайдено'}')
                trace_lvl += TRACE_ADD['notes']
                continue
            case c if c.startswith('ls'):
                contents = do_ls(current_loc)
                print('/'.join(current_loc))
                for c in contents:
                    print('|')
                    print('+-' + c)
            case c if c.startswith('cat'):
                file_name = do_cat(c, current_loc, 'server.txt')
                if not file_name:
                    continue
                if file_name in fragments_locs and file_name not in collected:
                    letter, idx = fragments_locs[file_name]
                    print(f'{GREEN}{FOUND_TEXT}{idx+1}: {letter}{RESET}')
                    fragments[idx] = letter
                    collected.add(file_name)
                if file_name == 'key_info.txt':
                    key_found = True
                    print(GREEN + FOUND_KEY + str(key) + RESET)
                trace_lvl += TRACE_ADD['cat']
            case c if c.startswith('cd'):
                new_loc = do_cd(c, current_loc, unlocked_dirs)
                if new_loc is None:
                    exited = True
                    break
                current_loc = new_loc
                trace_lvl += TRACE_ADD['cd']
                if current_loc[-1] == 'admin' and 'play назва-файлу' not in available_commands:
                    add_command(available_commands, 'play назва-файлу')
            case c if c.startswith('play'):
                res = do_play(c.split()[1], fragments_locs, current_loc, collected)
                if res is None:
                    exited = True
                    break
                trace_lvl += TRACE_ADD['play']
                if not res:
                    continue
                letter, idx = res
                print(f'{GREEN}{FOUND_TEXT}{idx+1}: {letter}{RESET}')
                fragments[idx] = letter
                collected.add(c.split()[1])
            case c if c.startswith('decrypt notes'):
                user_key = c.split('decrypt notes')[1].strip()
                do_decrypt(user_key, fragments, key_found, key, answer)
            case c if c.startswith('unlock'):
                user_pass = c.split()[1]
                if user_pass.lower() == answer.lower():
                    break
                tries += 1
                print(f'{RED}[X] Неправильний пароль. \
Залишилось спроб: {UNLOCK_TRIES - tries}{RESET}')
            case _:
                print(WRONG_COMMAND)
    if exited:
        print(EXIT_MESSAGE)
        return
    if trace_lvl >= MAX_TRACE_LVL:
        print(f'{RED}[!!!] ТРАСУВАННЯ: {trace_lvl}%/{MAX_TRACE_LVL}%{RESET}')
        print(f'{RED}Екран гасне. Рядок за рядком система стирає твою сесію.{RESET}')
        print(f'{RED}{BOLD}[sysadmin] Попався.{RESET}')
        print(RED + '*' * 15 + 'КІНЕЦЬ: ТЕБЕ ЗНАЙШЛИ' + '*' * 15 + RESET)
        return
    if tries >= UNLOCK_TRIES:
        print(f'{RED}[!!!] Неправильний пароль. Спроб не залишилось.{RESET}')
        print(f'{RED}Сховище запускає самознищення. Усі дані стерто назавжди.{RESET}')
        print(RED + '*' * 15 + 'КІНЕЦЬ: ДОКАЗИ ЗНИЩЕНО' + '*' * 15 + RESET)
        return

    print(f'{GREEN}[+] ПАРОЛЬ ПРИЙНЯТО. СХОВИЩЕ ВІДКРИТО.{RESET}')
    print(f'{GREEN}Ти копіюєш архів проєкту й розриваєш з\'єднання.{RESET}')
    print(f'{GREEN}Трасування: {trace_lvl}%   Кількість невдалих спроб: {tries}{RESET}')


def main() -> None:
    """Точка входу в гру"""
    play_game()


if __name__ == '__main__':
    main()
