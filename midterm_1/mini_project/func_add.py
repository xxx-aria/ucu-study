init_command = input()

MAX_PAPER_OUTPUT = 50
TONNER_DRAFT = 1
TONNER_NORM = 2
TONNER_BEST = 4

paper = 0
tonner = 0
MAX_PAPER_INPUT = 250
MAX_TONNER_INPUT = 200

loaded_count = 0
print_count = 0

# statistics
draft_count = 0
normal_count = 0
best_count = 0
paper_used = 0
tonner_used = 0
take_count = 0
unfinished_count = 0
canceled_count = 0

eco_mode = False

# in mm
PAPER_WIDTH = 210
PAPER_HEIGHT = 297

if init_command == 'on':
    is_on = True
    print('[ГОТОВО]')
    print(f'Папір: {paper} арк | Тонер: {tonner} мл')

    while is_on:

        command = input('Оберіть команду:')

        ml_factor = 0
        match command:
            case 'draft':
                ml_factor = TONNER_DRAFT
            case 'normal':
                ml_factor = TONNER_NORM
            case 'best':
                if eco_mode:
                    print('У режимі економії тонера best недоступний.')
                    canceled_count += 1
                    continue
                ml_factor = TONNER_BEST
            case 'add paper':
                raw = input('Введіть кількість аркушів:')
                try:
                    papers_to_add = int(raw)
                except ValueError:
                    print('Введіть додатне ціле число.')
                    continue
                if papers_to_add <= 0:
                    print('Введіть додатне ціле число.')
                    continue

                space_left = MAX_PAPER_INPUT - paper
                if space_left == 0:
                    print('Лоток подачі вже повний.')

                if space_left < papers_to_add:
                    print(f'Додано {space_left} арк. Не помістилося: {papers_to_add - space_left} арк.')
                    paper = MAX_PAPER_INPUT
                else:
                    print(f'Додано {papers_to_add} арк.')
                    paper += papers_to_add

                print(f'Папір: {paper} арк | Тонер: {tonner} мл')
                continue
            case 'add toner':
                raw = input('Введіть обʼєм тонера:')
                try:
                    tonner_to_add = int(raw)
                except ValueError:
                    print('Введіть додатне ціле число.')
                    continue
                if tonner_to_add <= 0:
                    print('Введіть додатне ціле число.')
                    continue

                space_left = MAX_TONNER_INPUT - tonner
                if space_left == 0:
                    print('Картридж вже повний.')

                if space_left < tonner_to_add:
                    print(f'Додано {space_left} мл тонера. Не помістилося: {tonner_to_add - space_left} мл.')
                    tonner = MAX_TONNER_INPUT
                else:
                    print(f'Додано {tonner_to_add} мл тонера.')
                    tonner += tonner_to_add

                print(f'Папір: {paper} арк | Тонер: {tonner} мл')
                continue
            case 'refill':
                if paper == MAX_PAPER_INPUT:
                    print('Лоток подачі вже повний.')
                else:
                    print(f'Лоток подачі поповнено до максимуму. Додано {MAX_PAPER_INPUT - paper} арк.')
                    paper = MAX_PAPER_INPUT

                if tonner == MAX_TONNER_INPUT:
                    print('Картридж вже повний.')
                else:
                    print(f'Картридж поповнено до максимуму. Додано {MAX_TONNER_INPUT - tonner} мл тонера.')
                    tonner = MAX_TONNER_INPUT

                print(f'Папір: {paper} арк | Тонер: {tonner} мл')
                continue
            case 'take':
                if loaded_count != 0:
                    loaded_count = 0
                    take_count += 1
                print('Лоток порожній.')
                continue
            case 'eco on':
                if eco_mode:
                    print('Режим економії тонера вже увімкнено.')
                else:
                    eco_mode = True
                    print('Режим економії тонера увімкнено.')
                continue
            case 'eco off':
                if not eco_mode:
                    print('Режим економії тонера вже вимкнено.')
                else:
                    eco_mode = False
                    print('Режим економії тонера вимкнено.')
                continue
            case 'selftest':
                print('-' * 20 + 'САМОДІАГНОСТИКА' + '-' * 20)

                paper_percent = paper * 100 // MAX_PAPER_INPUT
                tonner_percent = tonner * 100 // MAX_TONNER_INPUT

                print(f'Рівень ресурсів. Папір: {paper}/{MAX_PAPER_INPUT} арк. ({paper_percent}%) | Тонер: {tonner}/{MAX_TONNER_INPUT} мл ({tonner_percent}%)')
                print(f'Лоток виводу: {loaded_count} арк. (вільно {MAX_PAPER_OUTPUT - loaded_count})')
                print(f'Режим економії тонера: {'увімкнено' if eco_mode else 'вимкнено'}')
                print('Кількість аркушів, на яку вистачить тонера для друку у кожному режимі.')

                if eco_mode:
                    print(f'draft: {(tonner // TONNER_DRAFT) * 2} арк. | normal: {(tonner // TONNER_NORM) * 2} арк. | best: недоступно.')
                else:
                    print(f'draft: {tonner // TONNER_DRAFT} арк. | normal: {tonner // TONNER_NORM} арк. | best: {tonner // TONNER_BEST} арк.')

                is_problem = False
                if paper <= 0:
                    print('Докладіть папір: лоток подачі порожній.')
                    is_problem = True
                elif paper_percent < 10:
                    print('Паперу мало, варто докласти.')
                    is_problem = True
                if tonner <= 0:
                    print('Долийте тонер: картридж порожній.')
                    is_problem = True
                elif tonner_percent < 10:
                    print('Тонера мало, варто долити.')
                    is_problem = True
                if loaded_count >= MAX_PAPER_OUTPUT:
                    print('Заберіть роздруківки.')
                    is_problem = True

                if not is_problem:
                    print('Проблем не виявлено.')

                print('-' * 54)
                continue
            case 'poster':
                width = input('Введіть ширину постера (см):')
                try:
                    width = int(width) * 10 # converting cm to mm
                except ValueError:
                    print('Введіть додатне ціле число.')
                    canceled_count += 1
                    continue
                if width <= 0:
                    print('Введіть додатне ціле число.')
                    canceled_count += 1
                    continue

                height = input('Введіть висоту постера (см):')
                try:
                    height = int(height) * 10
                except ValueError:
                    print('Введіть додатне ціле число.')
                    canceled_count += 1
                    continue
                if height <= 0:
                    print('Введіть додатне ціле число.')
                    canceled_count += 1
                    continue

                book_height = height // PAPER_HEIGHT + (height % PAPER_HEIGHT != 0)
                book_width = width // PAPER_WIDTH + (width % PAPER_WIDTH != 0)
                book_count = book_height * book_width

                album_height = height // PAPER_WIDTH + (height % PAPER_WIDTH != 0)
                album_width = width // PAPER_HEIGHT + (width % PAPER_HEIGHT != 0)
                album_count = album_height * album_width

                if book_count <= album_count and book_height <= 26:
                    poster_papers = book_count
                elif book_count > album_count and album_height <= 26:
                    poster_papers = album_count
                else:
                    print('Постер зависокий: потрібно більше 26 рядів (A–Z).')
                    canceled_count += 1
                    continue

                poster_tonner = poster_papers * TONNER_NORM

                if poster_papers > MAX_PAPER_OUTPUT:
                    print(f'Постер завеликий: потрібно {poster_papers} арк.')
                    canceled_count += 1
                    continue
                if poster_papers > paper:
                    print(f'Недостатньо паперу: потрібно {poster_papers} арк.')
                    canceled_count += 1
                    continue
                if poster_tonner > tonner:
                    print(f'Недостатньо тонера: потрібно {poster_tonner} мл.')
                    canceled_count += 1
                    continue
                if poster_papers > MAX_PAPER_OUTPUT - loaded_count:
                    print('Лоток виводу не вмістить усі частини. Заберіть роздруківки.')
                    canceled_count += 1
                    continue

                if book_count <= album_count:
                    print(f'Орієнтація: книжкова. Сітка: {book_height} × {book_width} = {book_count} арк.')

                    print('+' + '----+' * book_width)
                    for row in range(book_height):
                        print('|' + '    |' * book_width)
                        letter = chr(ord('A') + row)
                        print('|', end='')
                        for column in range(1, book_width + 1):
                            print(' ' + letter + str(column) + ' |', end='')
                        print()
                        print('|' + '    |' * book_width)
                        print('+' + '----+' * book_width)
                else:
                    print(f'Орієнтація: альбомна. Сітка: {album_height} × {album_width} = {album_count} арк.')

                    print('+' + '------+' * album_width)
                    for row in range(album_height):
                        letter = chr(ord('A') + row)
                        print('|', end='')
                        for column in range(1, album_width + 1):
                            print('  ' + letter + str(column) + '  |', end='')
                        print()
                        print('+' + '------+' * album_width)

                paper -= poster_papers
                paper_used += poster_papers

                tonner -= poster_tonner
                tonner_used += poster_tonner

                loaded_count += poster_papers
                print_count += 1
                normal_count += 1

                print(f'Постер надруковано на {poster_papers} арк.')

                continue
            case 'off':
                print('=' * 20 + 'СТАТИСТИКА ДНЯ' + '=' * 20)

                print(f'draft: {draft_count} док. | normal: {normal_count} док. | best: {best_count} док.')
                popular = max(draft_count, normal_count, best_count)
                if popular != 0:
                    popular_name = ''
                    if draft_count == popular:
                        popular_name += 'draft'
                    if normal_count == popular:
                        if popular_name:
                            popular_name += ', '
                        popular_name += 'normal'
                    if best_count == popular:
                        if popular_name:
                            popular_name += ', '
                        popular_name += 'best'
                    print(f'Найпопулярніший режим: {popular_name} ({popular} док.)')
                else:
                    print('Найпопулярніший режим: відсутній.')

                print(f'Витрачено паперу: {paper_used} арк. | Витрачено тонера: {tonner_used} мл.')
                print(f'Роздруківки забирали (разів): {take_count}')
                print(f'Часткових друків: {unfinished_count} | Відмов: {canceled_count}')

                print('=' * 54)

                print(f'Виконано друків:{print_count}.')
                is_on = False
                continue
            case _:
                print('НЕВІДОМА КОМАНДА')
                continue

        if paper <= 0:
            print('Папір закінчився.')
            canceled_count += 1
            continue

        if tonner < ml_factor:
            print('Недостатньо тонера.')
            canceled_count += 1
            continue

        if loaded_count >= MAX_PAPER_OUTPUT:
            print('Лоток виводу повний. Заберіть роздруківки.')
            canceled_count += 1
            continue

        raw = input('Введіть кількість аркушів:')
        try:
            papers_to_print = int(raw)
        except ValueError:
            print('Введіть додатне ціле число.')
            canceled_count += 1
            continue

        if papers_to_print <= 0:
            print('Введіть додатне ціле число.')
            canceled_count += 1
            continue

        tonner_pages = papers_to_print
        if eco_mode:
            tonner_pages = (tonner_pages + 1) // 2

        tonner_needed = ml_factor * tonner_pages

        if (tonner_needed > tonner
            and papers_to_print <= paper
            and loaded_count + papers_to_print <= MAX_PAPER_OUTPUT
            and command != 'draft'
        ):
            if TONNER_NORM * tonner_pages <= tonner:
                print_choice = input('Можу надрукувати повністю в режимі normal. Друкувати? (yes/no)')
                match print_choice:
                    case 'yes':
                        ml_factor = TONNER_NORM
                        command = 'normal'
                    case 'no':
                        print('Відмова друку.')
                        canceled_count += 1
                        continue
                    case _:
                        print('Некоректна відповідь. Друк скасовано.')
                        canceled_count += 1
                        continue
            elif TONNER_DRAFT * tonner_pages <= tonner: # case eligable for eco mode
                print_choice = input('Можу надрукувати повністю в режимі draft. Друкувати? (yes/no)')
                match print_choice:
                    case 'yes':
                        ml_factor = TONNER_DRAFT
                        command = 'draft'
                    case 'no':
                        print('Відмова друку.')
                        canceled_count += 1
                        continue
                    case _:
                        print('Некоректна відповідь. Друк скасовано.')
                        canceled_count += 1
                        continue

        papers_printed = 0
        error_message = ''
        while papers_printed < papers_to_print:
            if paper <= 0:
                error_message = 'Папір закінчився.'
                break
            if tonner < ml_factor and not (eco_mode and papers_printed % 2 == 1):
                error_message = 'Недостатньо тонера.'
                break
            if loaded_count >= MAX_PAPER_OUTPUT:
                error_message = 'Лоток виводу повний. Заберіть роздруківки.'
                break

            paper -= 1
            paper_used += 1

            loaded_count += 1
            papers_printed += 1

            if eco_mode and papers_printed % 2 == 0:
                continue
            tonner -= ml_factor
            tonner_used += ml_factor

        if papers_to_print == papers_printed:
            print_count += 1
            print(f'Документ {command} надруковано.')

            if command == 'draft':
                draft_count += 1
            elif command == 'normal':
                normal_count += 1
            else:
                best_count += 1
        else:
            print(f'Надруковано {papers_printed} з {papers_to_print} арк.')
            print(error_message)
            unfinished_count += 1

print('[ПРИНТЕР ВИМКНЕНО]')
