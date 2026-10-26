'''
Lab assignment: read an admission rating list from a file
and write it to a file in CSV format.

Add type hints to both functions for all parameters
and return values.
'''


def read_input_file(pathname: str, number: int) -> list[list]:
    '''
    Read the admission rating list from a text file pathname
    and return a list of lists of strings for the first number students.

    The nested list for one student looks like:
    [rank, full name, admission mark ('+' or '—'), total score, school certificate average]
    All elements are strings. The full name (surname with initials) is a single string.

    Precondition: 0 <= number. If number exceeds the number of students
    in the file, all records are returned.

    >>> import tempfile, os
    >>> content = ('#\\tПІБ\\tС\\tΣ\\tДЕТАЛІЗАЦІЯ\\tКО\\tКВ\\tД\\n'
    ...     '1\\tМацюк М. І.\\tДо наказу\\t197.859\\t Математика (ЗНО) 197.00\\n'
    ...     ' Середній бал документа про освіту 10.80\\nРК: 1.01\\nСК: —\\n—\\t+\\n'
    ...     '2\\tПроць О. В.\\tДо наказу\\t197.152\\t Математика (ЗНО) 189.00\\n'
    ...     ' Середній бал документа про освіту 11.60\\nРК: 1.01\\nСК: —\\n—\\t+')
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(content)
    >>> read_input_file(tmp.name, 0)
    []
    >>> read_input_file(tmp.name, 1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file(tmp.name, 5)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60']]
    >>> os.remove(tmp.name)
    '''

    students = []
    if number == 0:
        return students

    with open(pathname, mode='r', encoding='utf-8') as f:
        while (line := f.readline()) != '' and len(students) < number:
            line = line.split('\t')
            if not line[0].isdigit(): # skip non-students (e.g. headers)
                continue

            school_line = f.readline()
            # skip lines with separate subject's ZNO scores
            while not school_line.strip().startswith('Середній бал'):
                school_line = f.readline()
            school_avg = school_line.split()[-1]

            mark_line = f.readline()
            while not mark_line.startswith('—'):  # admission mark line: — + / — -
                mark_line = f.readline()
            mark = mark_line.split()[-1]

            student = line[0:2] + [mark] + [line[3]] + [school_avg]
            students.append(student)

    return students


def write_csv_file(pathname: str, csv_pathname: str) -> None:
    '''
    Write the WHOLE content of the input file pathname to the file
    csv_pathname in CSV format
    (https://en.wikipedia.org/wiki/Comma-separated_values).
    The first line is a header. The function returns nothing.

    This function must use read_input_file.
    Using the csv module of the standard library is forbidden.

    >>> import tempfile, os
    >>> content = ('1\\tМацюк М. І.\\tДо наказу\\t197.859\\t Математика (ЗНО) 197.00\\n'
    ...     ' Середній бал документа про освіту 10.80\\nРК: 1.01\\nСК: —\\n—\\t+')
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
    ...     _ = tmp.write(content)
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as out:
    ...     pass
    >>> write_csv_file(tmp.name, out.name)
    >>> with open(out.name, encoding='utf-8') as csvfile:
    ...     print(csvfile.read().rstrip())
    №,ПІБ,Д,Заг.бал,С.б.док.осв.
    1,Мацюк М. І.,+,197.859,10.80
    >>> os.remove(tmp.name)
    >>> os.remove(out.name)
    '''

    students = read_input_file(pathname, float('inf'))

    with open(csv_pathname, mode='w', encoding='utf-8') as f:
        f.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        f.writelines([','.join(st) + '\n' for st in students])


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())

    write_csv_file('total.txt', 'total.csv')
