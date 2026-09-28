init_command = input()

MAX_PAPER = 50
TONNER_DRAFT = 1
TONNER_NORM = 2
TONNER_BEST = 4

paper = 0
tonner = 0
loaded_count = 0
print_count = 0

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

                tonner += tonner_to_add
                print(f'Папір: {paper} арк | Тонер: {tonner} мл')
                continue
            case 'take':
                loaded_count = 0
                print('Лоток порожній.')
                continue
            case 'off':
                print(f'Виконано друків:{print_count}.')
                is_on = False
                continue
            case _:
                print('НЕВІДОМА КОМАНДА')
                continue

        if paper <= 0:
            print('Папір закінчився.')
            continue

        if ml_factor * 1 > tonner:
            print('Недостатньо тонера.')
            continue

        if loaded_count >= MAX_PAPER:
            print('Лоток виводу повний. Заберіть роздруківки.')
            continue

        raw = input('Введіть кількість аркушів:')
        try:
            papers_to_print = int(raw)
        except ValueError:
            print('Введіть додатне ціле число.')
            continue

        if papers_to_print <= 0:
            print('Введіть додатне ціле число.')
            continue

        papers_printed = 0
        error_message = ''
        while papers_to_print > 0:
            if paper <= 0:
                error_message = 'Папір закінчився.'
                break
            if tonner <= 0:
                error_message = 'Недостатньо тонера.'
                break
            if loaded_count >= MAX_PAPER:
                error_message = 'Лоток виводу повний. Заберіть роздруківки.'
                break
            paper -= 1
            tonner -= ml_factor
            loaded_count += 1
            papers_to_print -= 1
            papers_printed += 1

        if papers_to_print <= 0:
            print_count += 1
            print(f'Документ {command} надруковано.')
        else:
            print(f'Надруковано {papers_printed} з {papers_to_print} арк.')
            print(error_message)
            papers_to_print = 0


print('[ПРИНТЕР ВИМКНЕНО]')
