"""root"""

import random
import time

UNLOCK_TRIES = 3

WRONG_COMMAND = '[?] Невідома команда.'
EXIT_MESSAGE = '[EXIT] Дякую за гру!'

COMMANDS_HELP = {
    'help': 'Перелік і пояснення усіх доступних команд',
    'notes': 'Переглянути твої зібрані фрагменти',
    'exit': 'Закінчити гру',
    'cd назва-папки': 'Перейти в папку',
    'cd ..': 'Перейти назад в минулу папку (на рівень вище)',
    'ls': 'Файли і папки, які є у папці, де ти знаходишся',
    'cat назва-файлу': 'Прочитати вміст файлу',
    'decrypt notes ключ': 'Побачиш справжній пароль; працює лише при повному notes',
    'unlock пароль': f'Відкрити сховище (пароль вже розшифрований); всього є {UNLOCK_TRIES} спроби',
    'play назва-файлу': 'Зіграти гру; працює лише з файлами з розширенням .game',
}


MAX_TRACE_LVL = 100
TRACE_ADD = {'cat': 5, 'cd': 2, 'notes': 3}

FOUND_TEXT = '[+] Знайдено фрагмент #'
FOUND_KEY = '[+] Знайдено ключ - '

DIARY_PASS = random.choice(['qwerty', 'abc', 'cool', 'wow', 'nowhere']) + str(
    random.randint(100, 999)
)

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
                'content': {
                    'ALL_I_FOUND.txt': {
                        'type': 'file',
                        'content': f'Я впевнений, що у щоденнику (diary) нашого сисадміна знаходиться дещо цікаве...\nЗміг дізнатись пароль: {DIARY_PASS}',
                    }
                },
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
    'net.game': '[NET] Десь у мережі 5×5 прихований канал зв\'язку - 3 клітинки поруч\nВводь координати (напр. B3), щоб просканувати сектор.\n[крапка = порожньо (мимо), X = сигнал]',
    'fw.game': '[FW] Фаєрвол тримає 5 вузлів, тобі потрібно вимкнути всі вузли (○ ○ ○ ○ ○).\n[● - активний, ○ - вимкнений]\nВведи номер вузла [1–5], щоб перемкнути його і сусідні вузли.\nУвага! Сусідні вузли також перемикаються. Тобто за один хід перемикається 2 або 3 вузли.',
    'port.game': '[PORT] Один порт від 1000 до 9999 відкритий.\nВведи номер порту - система підкаже "вище" чи "нижче" тобі потрібно змінити здогадку.',
    'ids.game': '[IDS] Система перевіряє, чи ти бот.\n На екрані з\'явиться код - введи його ТОЧНО і швидко (до 5 секунд). Потрібно 3 успіхи поспіль.\n Помилка - серія з нуля.',
}


def get_fragments_locations(answer: str) -> dict[str, tuple[str, int]]:
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


def unlock_diary() -> bool:
    print(
        '[!] Папку diary захищено особистим паролем сисадміна. Можливо, варто перевірити листування.'
    )
    print('Введіть пароль або q, щоб вийти.')
    guess = input('>>> ').strip()
    if guess.lower() == 'q':
        return False
    if guess != DIARY_PASS:
        print('[X] Неправильний пароль.')
        return False
    print('[+] Пароль прийнято.')
    return True


# =================


def guess_admin_pin() -> bool:
    print('[!] Папку admin захищено особистим PIN-кодом.')
    pin = str(random.randint(1000, 9999))
    print('PIN-код складається з 4 цифр.')
    print('Кількість спроб необмежена. Напишіть q, щоб припинити вгадування.')
    while (guess := input('>>> ').strip()) != pin:
        if guess.lower() == 'q':
            return False
        if len(guess) != 4 or not guess.isdigit():
            print('Неправильний формат.')
            continue

        if guess == pin:
            break

        are_present = 0
        at_pos = 0
        for i in range(4):
            if guess[i] in pin and guess[: i + 1].count(guess[i]) <= pin.count(guess[i]):
                are_present += 1
            if guess[i] == pin[i]:
                at_pos += 1

        print('Невдала спроба.')
        print(f'Цифр, які є у PIN-коді: {are_present}')
        print(f'Цифр на своїх позиціях: {at_pos}')
    print('[+] PIN прийнято. Доступ відкрито.')
    return True


def get_connection_matrix(n):
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


def print_connection_matrix(connection_matrix):
    n = len(connection_matrix)
    print('   ' + '   '.join([chr(o) for o in range(ord('A'), ord('A') + n)]))
    print(' +' + '---+' * n)
    for i, row in enumerate(connection_matrix):
        row = ['X' if x == 1 else '.' if x == -1 else ' ' for x in row]
        print(str(i + 1) + '| ' + ' | '.join(row) + ' |')
        print(' +' + '---+' * n)


def sea_battle():
    connection_matrix = get_connection_matrix(5)
    user_matrix = [[0] * 5 for _ in range(5)]
    left = 3
    while left > 0:
        print_connection_matrix(user_matrix)
        print('Введи координату для пострілу (напр. C4).')
        user_coord = input('>>> ').strip()
        if user_coord == 'exit':
            return False
        if len(user_coord) != 2:
            print('Неправильна координата.')
            continue
        if not user_coord[0].isalpha() or not user_coord[1].isdigit():
            print('Неправильна координата.')
            continue
        user_coord = user_coord.upper()
        num_i = int(user_coord[1]) - 1
        letter_j = ord(user_coord[0]) - ord('A')
        if not 0 <= num_i < 6 or not 0 <= letter_j < 6:
            print('Неправильна координата.')
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


def do_switch(seq, i):
    seq[i] = not seq[i]
    if i < 4:
        seq[i + 1] = not seq[i + 1]
    if i > 0:
        seq[i - 1] = not seq[i - 1]


def get_random_seq():
    seq = [True] * 5
    for i in range(random.randint(1, 5)):
        i = random.randint(0, 4)
        do_switch(seq, i)
    if seq == [True] * 5:
        return None
    return seq


def turn_off_firewall():
    circle = "○"
    full_circle = "●"
    while not (seq := get_random_seq()):
        continue
    while seq != [True] * 5:
        print(''.join([circle if x else full_circle for x in seq]))
        print('Введіть номер лампочки, яку перемкнути [1 - 5].')
        user_inp = input('>>> ').strip()
        if user_inp == 'exit':
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


def find_port():
    port = random.randint(1000, 9999)
    while True:
        guess = input('>>> ').strip()
        if guess == 'exit':
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
            print('Порт знайдено: {port}.')
            return True


def bypass_system():
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
            return False
        if user_inp.strip() != random_combo:
            print('Неправильно.')
            continue
        if t2 - t1 > 5:
            print(f'Запізно: {t2-t1:.2f} с.')
            continue
        words -= 1
    return True


def do_play(file_name, fragments_locs, curr_loc):
    if curr_loc[-1] != 'admin' or file_name not in fragments_locs:
        print('[X] Файл не знайдено.')
        return None
    letter, idx = fragments_locs[file_name]
    print(GAMES_DESCR[file_name])
    match file_name:
        case 'net.game':
            res = sea_battle()
        case 'fw.game':
            res = turn_off_firewall()
        case 'port.game':
            res = find_port()
        case 'ids.game':
            res = bypass_system()
    if res:
        return letter, idx
    print(f'[Q] Ви вийшли з мінігри {file_name}.')
    return None


# =================


def print_location(curr_loc: list[str], trace_lvl: int) -> str:
    print(
        '\nroot@nowhere:' + '\\'.join(curr_loc) + '$' + f' [TRACING {trace_lvl}%/{MAX_TRACE_LVL}%]'
    )


def get_answer(answers_file: str) -> str:
    answers = []
    with open(answers_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line := line.strip():
                answers.append(line)
    answer = random.choice(answers)
    return answer


def get_encrypted_answer(answer: str, shift: int = 0):
    return [chr(ord(l) + shift) for l in answer]


def print_intro() -> None:
    print('Три тижні тому сервер компанії NOWHERE зник з усіх мереж.', flush=True)
    time.sleep(2)
    print('Офіційно - його вимкнули.', flush=True)
    time.sleep(1.5)
    print('Неофіційно... ', end='', flush=True)
    time.sleep(2.5)
    print('він досі працює. ', end='', flush=True)
    time.sleep(1)
    print('І щось приховує.', flush=True)
    time.sleep(1)
    print('Натисни Enter, щоб продовжити...')
    while input('>>> '):
        print('Натисни Enter, щоб продовжити...')

    print('''Тобі вдалося зайти у систему. Ти - root.
Але адмін встиг заховати найважливіше: сховище політичних таємниць, закрите паролем.
Адмін також подбав про те, щоб більшість команд терміналу перестали працювати.
Пароль він розбив на зашифровані фрагменти й розкидав по системі.''')
    print('Натисни Enter, щоб рухатись далі...')
    while input('>>> '):
        print('Натисни Enter, щоб рухатись далі...')
    print(
        '''ТВОЯ МЕТА:
\tЗнайди всі фрагменти пароля (символи), розшифруй їх
\tі відкрий сховище. У тебе лише 3 спроби ввести пароль.
ЯК ГРАТИ:
\t- Ти вводиш команди, як у справжньому терміналі. На кожному етапі будуть відкриватись нові команди.
\t- Слідкуй за підказками системи, гра буде розвиватись поступово.
\t- Вийти з гри будь-коли - exit
ОБЕРЕЖНО:
\tКожна дія підвищує рівень ТРАСУВАННЯ (виводиться у форматі <tracing-lvl>%/100% при кожному запиті).
\tЯкщо він дійде до 100% - тебе знайдуть.\n''',
        flush=True,
    )
    time.sleep(5)
    print('Натисни Enter, щоб підключитися...')
    while input('>>> '):
        print('Натисни Enter, щоб підключитися...')
    print('SYSTEM BOOT SEQUENCE INITIATED.\nLaunching NOWHERE OS... ', end='', flush=True)
    time.sleep(1)
    print('[OK]')
    print('Loading core modules... ', end='', flush=True)
    time.sleep(1)
    print('[OK]')
    print('Checking hardware integrity... ', end='', flush=True)
    time.sleep(1)
    print('[OK]')
    print('Establishing secure uplink... ', end='', flush=True)
    time.sleep(1)
    print('Connected.')
    print('\nNOWHERE is fully operational. Welcome back, root.', flush=True)
    time.sleep(2)
    print('CRITICAL ERROR: Received foreign message [press Enter].')
    while input('>>> '):
        print('Натисни Enter, щоб прочитати повідомлення...')
    print('''?: Привіт, root. Радий тебе знову бачити. Покладаюсь на тебе.
Щоб дізнатись про взаємодію з системою введи наступну команду:
\tcat readme.txt''')


def add_command(curr_commands: list[str], command: str) -> None:
    command = command.strip().lower()
    if command not in COMMANDS_HELP:
        return
    curr_commands.append(command)
    print(f'[НОВА КОМАНДА] Перегляньте, як працює команда {command}, ввівши help.')


def print_help(available_commands: list[str]) -> None:
    for c in available_commands:
        # match c:
        #     case 'cd':
        #         c += ' назва-папки'
        #     case 'cat':
        #         c += ' назва-файлу'
        #     case 'decrypt':
        #         c += ' notes ключ'
        #     case 'unlock':
        #         c += ' пароль'
        print(f'\t{c:<25}- {COMMANDS_HELP[c]}')


def do_ls(current_loc):
    loc = FILE_SYSTEM
    for x in current_loc[2:]:
        loc = loc[x]['content']
    return list(loc)


def do_cat(comm, current_loc, files_contents_pathname):
    file_name = comm.split()[1]
    if not file_name.endswith('.txt'):
        print('[X] Даний формат файлу не підтримується для читання')
        return None
    if file_name not in do_ls(current_loc):
        print('[X] Файл не знайдено')
        return None

    loc = FILE_SYSTEM
    for x in current_loc[2:]:
        loc = loc[x]['content']
    loc = loc[file_name]

    if loc.get('content', None):
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
                print(contents)
                return file_name

    print('[X] Файл не знайдено')
    return None


def do_cd(comm, location):
    curr_loc = FILE_SYSTEM
    for x in location[2:]:
        curr_loc = curr_loc[x]['content']
    dest = comm.split()[1]
    if dest == '..':
        if len(location) == 2:
            return location
        return location[:-1]
    if dest not in curr_loc:
        print(f'[X] Неправильна команда: папки {dest} не існує')
        return location
    if curr_loc[dest]['type'] != 'dir':
        print(f'[X] Неправильна команда: {dest} не є папкою')
        return location

    if dest == 'admin':
        if guess_admin_pin():
            return location + [dest]
        print('[X] Невдала спроба розблокування папки admin')
        return location

    if dest == 'diary':
        if unlock_diary():
            return location + [dest]
        print('[X] Невдала спроба розблокування папки diary')
        return location
    return location + [dest]


def is_valid_command(user_comm, available_commands):
    for comm in available_commands:
        if comm.split()[0] == user_comm.split()[0]:
            return len(comm.split()) == len(user_comm.split())
    return False


# =================


def play_game(key: int = 0) -> None:
    print('*' * 80)
    print(f'{'root@nowhere':^80}')
    print('*' * 80)

    current_loc = ['', 'home']
    available_commands = ['cat readme.txt', 'exit']

    answer = get_answer('words.txt')
    answer_encrypted = get_encrypted_answer(answer, key)

    fragments = ['_'] * len(answer)
    fragments_locs = get_fragments_locations(answer_encrypted)

    key_found = False
    trace_lvl = 0
    tries = 0

    print_intro()

    print_location(current_loc, trace_lvl)
    while (user_comm := input('>>> ').strip()) not in available_commands:
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

    while (user_comm := input('>>> ').strip()) not in available_commands:
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

    while trace_lvl <= MAX_TRACE_LVL and tries < UNLOCK_TRIES:

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
                print(EXIT_MESSAGE)
                return
            case 'notes':
                print('Зібрані символи:')
                print('\t' + ' '.join(fragments))
                print(f'Ключ: {key if key_found else 'ще не знайдено'}')
                trace_lvl += TRACE_ADD['notes']
                continue
            case c if c.startswith('ls'):
                contents = do_ls(current_loc)
                print('\\'.join(current_loc))
                for c in contents:
                    print('|')
                    print('+-' + c)
            case c if c.startswith('cat'):
                file_name = do_cat(c, current_loc, 'server.txt')
                if not file_name:
                    continue
                if file_name in fragments_locs:
                    letter, idx = fragments_locs[file_name]
                    print(f'{FOUND_TEXT}{idx+1}: {letter}')
                    fragments[idx] = letter
                if file_name == 'key_info.txt':
                    key_found = True
                    print(FOUND_KEY + str(key))
                trace_lvl += TRACE_ADD['cat']
            case c if c.startswith('cd'):
                current_loc = do_cd(c, current_loc)
                trace_lvl += TRACE_ADD['cd']
                if current_loc[-1] == 'admin' and 'play назва-файлу' not in available_commands:
                    add_command(available_commands, 'play назва-файлу')
            case c if c.startswith('play'):
                res = do_play(c.split()[1], fragments_locs, current_loc)
                if not res:
                    continue
                letter, idx = res
                print(f'{FOUND_TEXT}{idx+1}: {letter}')
                fragments[idx] = letter
            case c if c.startswith('decrypt notes'):
                user_key = c.split('decrypt notes')[1].strip()
                if '_' in fragments:
                    print('[X] Неможливо розшифрувати пароль: нотатки неповні.')
                    continue
                if not key_found:
                    print('[X] Неможливо розшифрувати пароль: ключ ще не знайдений.')
                    continue
                if user_key != key:
                    print('[X] Неможливо розшифрувати пароль: неправильний пароль.')
                    continue
                print('Дешифрування пароля', end='')
                time.sleep(0.5)
                print('.', end='')
                time.sleep(0.5)
                print('.', end='')
                time.sleep(0.5)
                print('.', end='')
                print(f'[PASSWORD] ПАРОЛЬ ДО СИСТЕМИ: {answer}')
                print('Скористайтеся командою unlock')
            case c if c.startswith('unlock'):
                user_pass = c.split('unlock').strip()
                if user_pass != answer:
                    tries += 1
                    continue

    if trace_lvl > MAX_TRACE_LVL:
        print(f'[!!!] ТРАСУВАННЯ: {trace_lvl}%/{MAX_TRACE_LVL}%')
        print('Екран гасне. Рядок за рядком система стирає твою сесію.')
        print('[sysadmin] Попався.')
        print('*' * 15 + 'КІНЕЦЬ: ТЕБЕ ЗНАЙШЛИ' + '*' * 15)
        return
    if tries >= UNLOCK_TRIES:
        print('[!!!] Неправильний пароль. Спроб не залишилось.')
        print('Сховище запускає самознищення. Усі дані стерто назавжди.')
        print('*' * 15 + 'КІНЕЦЬ: ДОКАЗИ ЗНИЩЕНО' + '*' * 15)
        return

    print('[+] ПАРОЛЬ ПРИЙНЯТО. СХОВИЩЕ ВІДКРИТО.')
    print('Ти копіюєш архів проєкту й розриваєш з\'єднання.')
    print(f'Трасування: {trace_lvl}%   Кількість невдалих спроб: {tries}')


if __name__ == '__main__':
    import random

    seed = random.randint(1, 100)
    play_game()
