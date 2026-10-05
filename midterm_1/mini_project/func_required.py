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
toner_used = 0
take_count = 0
unfinished_count = 0
canceled_count = 0

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
                    print(f'Найпопулярніший режим: відсутній.')

                print(f'Витрачено паперу: {paper_used} арк. | Витрачено тонера: {toner_used} мл.')
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

        tonner_needed = ml_factor * papers_to_print
        if (tonner_needed > tonner
            and papers_to_print <= paper
            and loaded_count + papers_to_print <= MAX_PAPER_OUTPUT
            and command != 'draft'
        ):
            if TONNER_NORM * papers_to_print <= tonner:
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
            elif TONNER_DRAFT * papers_to_print <= tonner:
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
            if tonner < ml_factor:
                error_message = 'Недостатньо тонера.'
                break
            if loaded_count >= MAX_PAPER_OUTPUT:
                error_message = 'Лоток виводу повний. Заберіть роздруківки.'
                break

            paper -= 1
            paper_used += 1

            tonner -= ml_factor
            toner_used += ml_factor

            loaded_count += 1
            papers_printed += 1

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
