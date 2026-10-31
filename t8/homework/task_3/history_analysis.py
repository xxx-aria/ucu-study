"""
Analysis of the Google Chrome browser history.

A visit is a tuple (url, title, date, time, duration):
url and title are str, date is "yyyy-mm-dd", time is "hh:mm:ss.ffffff",
duration is an int (microseconds). The list of visits may be
in any order, not necessarily chronological.
"""


def sites_on_date(visits: list, date: str) -> set[str]:
    """
    Returns the set of all urls that have been visited on the given date.

    :param visits: all visits in the browser history
    (you get it as the result of the function get_chrome_os
    from get_browser_history module)
    :param date: date in format "yyyy-mm-dd"
    :return: set of urls visited on date

    >>> visits = [('https://a.com/', 'A', '2024-10-01', '10:00:00.000000', 100),
    ...           ('https://b.com/', 'B', '2024-10-02', '11:00:00.000000', 300),
    ...           ('https://a.com/', 'A', '2024-10-02', '12:00:00.000000', 200)]
    >>> sites_on_date(visits, '2024-10-02') == {'https://a.com/', 'https://b.com/'}
    True
    >>> sites_on_date(visits, '2024-10-03')
    set()
    """

    visited_urls = set()
    for url, _, visit_date, _, _ in visits:
        if visit_date == date:
            visited_urls.add(url)
    return visited_urls


def most_frequent_sites(visits: list, number: int) -> set[str]:
    """
    Returns the set of 'number' most frequently visited urls.

    If several urls have the same number of visits, the urls that are
    smaller by the built-in string comparison are chosen first.
    If number is greater than the number of different urls, the set of
    all visited urls is returned.

    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites

    >>> visits = [('https://a.com/', 'A', '2024-10-01', '10:00:00.000000', 100),
    ...           ('https://b.com/', 'B', '2024-10-02', '11:00:00.000000', 300),
    ...           ('https://a.com/', 'A', '2024-10-02', '12:00:00.000000', 200)]
    >>> most_frequent_sites(visits, 1)
    {'https://a.com/'}
    >>> most_frequent_sites(visits, 5) == {'https://a.com/', 'https://b.com/'}
    True
    """

    visits_freq_by_url = {}
    for visit in visits:
        url = visit[0]
        num = visits_freq_by_url.get(url, 0)
        visits_freq_by_url[url] = num + 1

    visits_freq_by_num = {}
    for url, num in visits_freq_by_url.items():
        if num not in visits_freq_by_num:
            visits_freq_by_num[num] = []
        visits_freq_by_num[num].append(url)

    res = set()
    for num in sorted(visits_freq_by_num)[::-1]:
        urls = sorted(visits_freq_by_num[num])
        while len(urls) > 0 and number > 0:
            res.add(urls.pop(0))
            number -= 1
        if number <= 0:
            break

    return res


def get_url_info(visits: list, url: str) -> tuple:
    """
    Returns a tuple with info about the site with the given url:
    title - title of the site (from its last visit)
    last_visit_date - date of the last visit of this site, "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, "hh:mm:ss.ffffff"
    num_of_visits - how many times this site was visited
    average_time - average duration of a visit to this site

    If the url was not visited, title and last visit date/time are
    empty strings, number of visits and average time are zeros.

    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)

    >>> visits = [('https://a.com/', 'A', '2024-10-01', '10:00:00.000000', 100),
    ...           ('https://b.com/', 'B', '2024-10-02', '11:00:00.000000', 300),
    ...           ('https://a.com/', 'A', '2024-10-02', '12:00:00.000000', 200)]
    >>> get_url_info(visits, 'https://a.com/')
    ('A', '2024-10-02', '12:00:00.000000', 2, 150.0)
    >>> get_url_info(visits, 'https://c.com/')
    ('', '', '', 0, 0)
    """

    last_title = ''
    last_date = ''
    last_time = ''
    num = 0
    duration_sum = 0
    for visit_url, title, date, time, duration in visits:
        if visit_url != url:
            continue
        num += 1
        duration_sum += duration
        if not last_date or not last_time or not last_title:
            last_date = date
            last_time = time
            last_title = title
            continue

        if last_date > date:
            continue
        if last_date == date and last_time > time:
            continue

        last_date = date
        last_time = time
        last_title = title

    return (last_title, last_date, last_time, num, duration_sum / num if num else 0)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
