"""
Редагування статей для газети: поділ тексту на речення, виправлення
пробілів і великих літер, пошук можливих помилок і повторів слів.
"""

WORDS = {
    'а',
    'бо',
    'буває',
    'будь-які',
    'в',
    'важливі',
    'вам',
    'вже',
    'виходить',
    'вона',
    'відкрили',
    'газета',
    'давно',
    'де',
    'для',
    'дуже',
    'зала',
    'зміни',
    'золота',
    'кава',
    'києві',
    'кожному',
    'львові',
    'ми',
    'навчання',
    'навіть',
    'найкраща',
    'нам',
    'напишіть',
    'наша',
    'не',
    'неділю',
    'новий',
    'новини',
    'нову',
    'номері',
    'ніколи',
    'осінь',
    'пишемо',
    'поради',
    'порожня',
    'працює',
    'прийшли',
    'про',
    'разу',
    'розкладі',
    'смачна',
    'студенти',
    'та',
    'так',
    'там',
    'тепла',
    'тиха',
    'у',
    'уку',
    'формат',
    'холодна',
    'цього',
    'чекали',
    'чи',
    'ще',
    'щодня',
    'щомісяця',
    'є',
    'і',
    "інтерв'ю",
}

PUNCTUATION = ',.!?:;'

# Над кожною функцією вказано бали за функціональність:
# разом 6.4 бала, ще до 1.6 бала дає якість коду (pylint).


# 0.8 бала
def read_file(filepath: str) -> list[str]:
    """
    Зчитує текст статті з файлу.

    Кожен непорожній рядок файлу містить одне речення, яке закінчується
    знаком '.', '!' або '?' (знак лишається в кінці речення). Усередині
    речення цих знаків немає. Після речення в тому самому рядку може йти
    нотатка редактора, яка завжди починається з "ред." — її треба
    відкинути. Пробіли на початку і в кінці речення треба прибрати, інші
    пробіли всередині речення лишаються як є. Порожні рядки пропускаються.

    Аргументи:
        filepath: шлях до вхідного файлу

    Повертає:
        list[str]: речення в порядку файлу

    Приклад:
        >>> import tempfile, os
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
        ...                                  encoding='utf-8') as tmp:
        ...     _ = tmp.write("чи є  кава? ред. уточнити\\n\\n  вона дуже смачна .\\n")
        >>> read_file(tmp.name)
        ['чи є  кава?', 'вона дуже смачна .']
        >>> os.remove(tmp.name)
    """
    text = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line = line.split('ред.')[0].strip()
            text.append(line)
    return text


# 1.1 бала
def fix_sentence(sentence: str) -> str:
    """
    Виправляє речення (як його повертає read_file, тобто без пробілів на
    початку і в кінці): між словами лишає рівно один пробіл, прибирає
    пробіли перед знаками з PUNCTUATION і робить першу літеру речення
    великою (решту літер не змінює). Після знака завжди йде пробіл або
    кінець речення.

    Аргументи:
        sentence: речення

    Повертає:
        str: виправлене речення

    Приклад:
        >>> fix_sentence("так , кава є,  і вона дуже смачна .")
        'Так, кава є, і вона дуже смачна.'
        >>> fix_sentence("у Львові є УКУ : кава!")
        'У Львові є УКУ: кава!'
        >>> fix_sentence("Все добре.")
        'Все добре.'
    """
    res = []
    sentence = [x.strip() for x in sentence.split()]
    for i, w in enumerate(sentence):
        if i == 0 and w.isalpha():
            w = w.capitalize()
        if w in PUNCTUATION:
            res[-1] += w
            continue
        res.append(w)

    return ' '.join(res)


# 0.6 бала
def split_words(sentence: str) -> list[str]:
    """
    Ділить речення на слова. Знаки з PUNCTUATION не є частиною слів
    (після знака завжди йде пробіл або кінець речення), а апостроф
    і дефіс усередині слова — є (інтерв'ю, будь-які). Слова
    повертаються малими літерами.

    Аргументи:
        sentence: речення

    Повертає:
        list[str]: слова речення в порядку тексту

    Приклад:
        >>> split_words("Так, кава є, і вона смачна!")
        ['так', 'кава', 'є', 'і', 'вона', 'смачна']
        >>> split_words("Інтерв'ю про будь-які зміни.")
        ["інтерв'ю", 'про', 'будь-які', 'зміни']
    """
    words = []
    for w in sentence.lower().split(' '):
        if w[-1] in PUNCTUATION:
            w = w[:-1]
        words.append(w)
    return words


# 1.6 бала
def check_words(words: list[str]) -> tuple[dict[str, int], set[str]]:
    """
    Перевіряє слова одного речення: шукає можливі помилки і повтори.

    Аргументи:
        words: слова речення малими літерами в порядку тексту

    Повертає:
        tuple: (typos, repeats)
        - typos: словник, ключ — слово, якого немає в WORDS, значення —
          скільки разів воно трапляється в words; слова додаються до
          словника в порядку першої появи (вміст WORDS може змінитися,
          не покладайтеся на нього)
        - repeats: множина слів довших за 3 символи, які трапляються
          в words більше одного разу

    Приклад:
        >>> check_words(['чай', 'є', 'кава', 'кавва', 'і', 'чай', 'кава'])
        ({'чай': 2, 'кавва': 1}, {'кава'})
        >>> check_words(['там', 'є', 'там', 'є'])
        ({}, set())
        >>> typos, repeats = check_words(['осінь', 'у', 'львові', 'осінь', 'у', 'львові'])
        >>> sorted(repeats)
        ['львові', 'осінь']
    """
    typos = {}
    repeats = set()

    for w in words:
        if len(w) > 3 and words.count(w) > 1:
            repeats.add(w)

        if w in WORDS:
            continue

        w_count = typos.get(w, 0)
        typos[w] = w_count + 1

    return (typos, repeats)


# 1.1 бала
def edit_text(sentences: list[str]) -> list[tuple[str, dict[str, int], set[str]]]:
    """
    Редагує статтю: для кожного речення за допомогою попередніх функцій
    складає кортеж
        (виправлене речення, можливі помилки, повтори)
    де виправлене речення — з fix_sentence, а помилки і повтори —
    з check_words для слів цього речення (з split_words).
    Речення йдуть у тому самому порядку. Переданий список має лишитися
    без змін.

    Аргументи:
        sentences: речення (результат read_file)

    Повертає:
        list[tuple]: по одному кортежу на речення

    Приклад:
        >>> edit_text(["так , кава є, і кава смачна ."])
        [('Так, кава є, і кава смачна.', {}, {'кава'})]
        >>> report = edit_text(["чи є  кавва ?", "Кавва , кавва!"])
        >>> report[0]
        ('Чи є кавва?', {'кавва': 1}, set())
        >>> report[1]
        ('Кавва, кавва!', {'кавва': 2}, {'кавва'})
        >>> edit_text([])
        []
    """
    res = []
    for sentence in sentences:
        fixed = fix_sentence(sentence)
        typos, repeats = check_words(split_words(fixed))
        res.append(tuple((fixed, typos, repeats)))

    return res


# 1.2 бала
def write_report(report: list[tuple[str, dict[str, int], set[str]]], filepath: str) -> None:
    """
    Записує звіт у файл у порядку звіту: для кожного речення три рядки —
    виправлене речення, а під ним з відступом у 4 пробіли
        помилки: слово (кількість), слово (кількість)
        повтори: слово, слово
    Помилки йдуть у порядку словника, кожне слово з кількістю в дужках;
    повтори — в порядку, який дає sorted. Елементи розділені ', ';
    якщо помилок або повторів немає, рядок однаково має пробіл після
    двокрапки і на цьому закінчується ("    помилки: ").

    Аргументи:
        report: список кортежів у форматі результату edit_text
        filepath: шлях до файлу, куди записати звіт

    Приклад:
        >>> import tempfile, os
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as out:
        ...     pass
        >>> write_report([('Чи є кавва, кавва?', {'кавва': 2}, {'кавва'}),
        ...               ('Осінь, чай і кавва, кавва і осінь!', {'кавва': 2, 'чай': 1},
        ...                {'осінь', 'кавва'})], out.name)
        >>> with open(out.name, encoding='utf-8') as file:
        ...     print(file.read(), end='')
        Чи є кавва, кавва?
            помилки: кавва (2)
            повтори: кавва
        Осінь, чай і кавва, кавва і осінь!
            помилки: кавва (2), чай (1)
            повтори: кавва, осінь
        >>> write_report([('Кава є.', {}, set())], out.name)
        >>> with open(out.name, encoding='utf-8') as file:
        ...     file.readlines()
        ['Кава є.\\n', '    помилки: \\n', '    повтори: \\n']
        >>> os.remove(out.name)
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for req in report:
            fixed, typos, repeats = req
            typos_sorted = {t: typos[t] for t in sorted(typos)}
            repeats_sorted = sorted(list(repeats))
            f.write(fixed + '\n')
            f.write('    помилки: ')
            for typo, n in typos_sorted.items():
                f.write(f'{typo} ({n})')
                if not list(typos_sorted)[-1] == typo:
                    f.write(', ')
            f.write('\n')
            f.write('    повтори: ')
            f.write(', '.join(repeats_sorted))
            f.write('\n')


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
    write_report(edit_text(read_file("input.txt")), "output.txt")
