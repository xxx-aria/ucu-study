"""
Working with IMDb keywords: films and their keywords.
"""


def leave_keyword_from_file(file_input: str, keyword: str, file_output: str) -> int:
    """Writes to the output file only the films that have the given keyword.

    All the text before the keywords list (sections 1-7 and the header of
    section 8) is copied unchanged. In the keywords list, all the lines of
    a film are kept if one of them has the given keyword, otherwise all the
    lines of this film are removed.

    Args:
        file_input (str): The input file containing the keywords.
        keyword (str): The keyword the films in the output file must have.
        file_output (str): The output file to write the filtered keywords.

    Returns:
        int: The number of lines of the keywords list removed from the input file.

    Examples:
        >>> leave_keyword_from_file('keywords.list', 'friendship', 'keywords_updated.list')
        3725264
        >>> keywords = create_film_keywords_dictionary('keywords_updated.list')
        >>> sum(len(values) for values in keywords.values())
        233878
        >>> values = iter(keywords.items())
        >>> movie, keywords = next(values)
        >>> movie
        '"#ATown" (2014)'
        >>> keywords == {'friendship', 'texas', 'drugs', 'beer', 'austin-texas', 'love',
        ...              'web-series'}
        True
        >>> movie, keywords = next(values)
        >>> movie
        '"11-11 En mi cuadra nada cuadra" (2013)'
        >>> keywords == {'friendship', 'pop-star', 'movie-director', 'inventor', 'time-machine',
        ...              'geek', 'cooking', 'musician', 'price-of-fame', 'singing', 'star',
        ...              'mad-scientist', 'time-travel', 'missing-mother', 'teenage-love'}
        True
    """
    with open(file_input, 'r', encoding='latin-1') as f_in:
        with open(file_output, 'w', encoding='latin-1') as f_out:
            for line in f_in:
                f_out.write(line)
                if line.strip() == '8: THE KEYWORDS LIST':
                    f_out.write(f_in.readline())
                    f_out.write(f_in.readline())
                    break

            removed = 0
            curr_film = ''
            curr_lines = []
            curr_kws = set()
            for line in f_in:
                if not line.strip():
                    continue
                line_parts = list(
                    map(lambda x: x.strip(), filter(lambda x: x != '', line.split('\t')))
                )
                film, kw = line_parts[0], line_parts[-1]
                if film != curr_film:
                    if keyword in curr_kws:
                        f_out.writelines(curr_lines)
                    else:
                        removed += len(curr_lines)
                    curr_film = film
                    curr_kws = {kw}
                    curr_lines = [line]
                    continue
                curr_lines.append(line)
                curr_kws.add(kw)
        if keyword in curr_kws:
            f_out.writelines(curr_lines)
        else:
            removed += len(curr_lines)
        return removed


def create_film_keywords_dictionary(filename: str) -> dict[str, set[str]]:
    """Creates a dictionary where the key is the name of the movie
    and the year in brackets as in the file, and the values
    are the set of keywords.

    Args:
        filename (str): The name of the file containing the keywords.

    Returns:
        dict[str, set[str]]: A dictionary with movie names and years as keys
                             and sets of keywords as values.

    Examples:
        >>> keywords = create_film_keywords_dictionary('keywords.list')
        >>> sum(len(values) for values in keywords.values())
        3959142
        >>> values = iter(keywords.items())
        >>> next(values)
        ('"#1 Single" (2006)', {'number-in-title'})
        >>> next(values)
        ('"#1MinuteNightmare" (2014)', {'web-series'})
        >>> movie = next(values)
        >>> movie[0]
        '"#30Nods" (2016)'
        >>> movie[1] == {'friend', 'vlog', 'heroin'}
        True
    """
    films_kws = {}
    with open(filename, 'r', encoding='latin-1') as f:
        for line in f:
            if line.strip() != '8: THE KEYWORDS LIST':
                continue
            f.readline()
            f.readline()
            break

        for line in f:
            if not line.strip():
                continue
            line_parts = list(map(lambda x: x.strip(), filter(lambda x: x != '', line.split('\t'))))
            film, kw = line_parts[0], line_parts[-1]
            if film not in films_kws:
                films_kws[film] = set()
            films_kws[film].add(kw)

    return films_kws


def find_films_with_max_keywords(
    film_keywords: dict[str, set[str]], num_of_films: int
) -> list[tuple]:
    """Finds the films with the maximum number of keywords.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        num_of_films (int): The number of films to return.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the name of the film
                     and the number of keywords, sorted by the number of keywords
                     in descending order. If the numbers of keywords are equal,
                     the films are sorted by names with usual string comparison.

    Examples:
        >>> film_keywords = create_film_keywords_dictionary('keywords.list')
        >>> films = find_films_with_max_keywords(film_keywords, 3)
        >>> films[0]
        ('Clouds of Sils Maria (2014)', 642)
        >>> films[1:]
        [('The Dark Knight (2008)', 530), ('The Dark Knight Rises (2012)', 446)]
    """
    film_kw_num = list(map(lambda film: (film, len(film_keywords[film])), film_keywords))
    return sorted(film_kw_num, key=lambda x: (-x[1], x[0]))[:num_of_films]


def find_most_popular_keywords(film_keywords: dict, num_of_keywords: int) -> list[tuple]:
    """Finds the most popular keywords.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        num_of_keywords (int): The number of keywords to return.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the keyword
                     and the number of films associated with that keyword, sorted by
                     the number of films in descending order. If the numbers of films
                     are equal, the keywords are sorted with usual string comparison.

    Examples:
        >>> find_most_popular_keywords(create_film_keywords_dictionary('keywords.list'), 3)
        [('character-name-in-title', 40690), ('independent-film', 30772), ('based-on-novel', 28213)]
    """
    kws_dct = {}
    for f_kws in film_keywords.values():
        for kw in f_kws:
            kws_dct[kw] = kws_dct.get(kw, 0) + 1
    kws_list = list(map(lambda kw: (kw, kws_dct[kw]), kws_dct))
    return sorted(kws_list, key=lambda x: (-x[1], x[0]))[:num_of_keywords]


def find_films_keyword_year(film_keywords: dict, keyword: str, year: int) -> set:
    """Finds films that contain a specific keyword and were released in a specific year.

    A film was released in the year if its name contains the year in brackets,
    for example '(1988)'.

    Args:
        film_keywords (dict): A dictionary where the key is the name of the movie
                              and the year in brackets, and the values are sets of keywords.
        keyword (str): The keyword to search for.
        year (int): The year of release to search for.

    Returns:
        set: A set of film names that match the keyword and year.

    Examples:
        >>> films = create_film_keywords_dictionary('keywords.list')
        >>> find_films_keyword_year(films, 'supernatural', 1988) == {
        ...     'Kumander Bawang (1988)', '"Monsters" (1988) {Rain Dance (#1.19)}',
        ...     'Saturday the 14th Strikes Back (1988)', '"Tian xia" (1988)',
        ...     'A Nightmare on Elm Street 4: The Dream Master (1988)'}
        True
    """
    return set(filter(lambda f: f'({year})' in f and keyword in film_keywords[f], film_keywords))


if __name__ == '__main__':
    import doctest

    # with open('keywords.list', 'r', encoding='latin-1') as fin:
    #     with open('out.txt', 'w', encoding='utf-8') as fout:
    #         for line in fin:
    #             fout.write(line)

    print(doctest.testmod())
    # leave_keyword_from_file('keywords.list', 'nazis', 'output.list')

    # create_film_keywords_dictionary('keywords.list')

    # starts = set()
    # with open('keywords.list', 'r', encoding='latin-1') as fin:
    #     for line in fin:
    #         if line.strip() == '8: THE KEYWORDS LIST':
    #             fin.readline()
    #             fin.readline()
    #             print('reached')
    #             break
    #     for line in fin:
    #         if line:
    #             starts.add(line[0])
    #         else:
    #             print(line)
    # print(starts)
