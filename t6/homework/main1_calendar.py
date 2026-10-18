"""My lab"""

from calendar import TextCalendar, HTMLCalendar


def get_semester_calendar(
    output_type: str, year: int, first_month: int, last_month: int
) -> str | None:
    """
    Return months calendar of the semester in specified months range in txt or html format.

    If output type is neither "txt" nor "html", return None.
    If year is not a positive integer or months are not in months range, return None,
    and if last month is less than first, return None.

    >>> get_semester_calendar("txt", 2024, 10, 10)
    '    October 2024\\nMo Tu We Th Fr Sa Su\\n    1  2  3  4  5  6\\n 7  8  9 10 11 12 13\\n\
14 15 16 17 18 19 20\\n21 22 23 24 25 26 27\\n28 29 30 31\\n'
    >>> get_semester_calendar("html", 2024, 10, 10)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n\
<tr><th colspan="7" class="month">October 2024</th></tr>\\n<tr><th class="mon">Mon</th>\
<th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th>\
<th class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp;</td>\
<td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td>\
<td class="sat">5</td><td class="sun">6</td></tr>\\n<tr><td class="mon">7</td>\
<td class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri">11</td>\
<td class="sat">12</td><td class="sun">13</td></tr>\\n<tr><td class="mon">14</td>\
<td class="tue">15</td><td class="wed">16</td><td class="thu">17</td><td class="fri">18</td>\
<td class="sat">19</td><td class="sun">20</td></tr>\\n<tr><td class="mon">21</td>\
<td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td class="fri">25</td>\
<td class="sat">26</td><td class="sun">27</td></tr>\\n<tr><td class="mon">28</td>\
<td class="tue">29</td><td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td>\
<td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\\n</table>\\n'
    >>> get_semester_calendar("png", 2024, 10, 10)
    >>> get_semester_calendar("txt", -1, 10, 10)
    >>> get_semester_calendar("txt", 2026, 10, 100)
    >>> get_semester_calendar("html", 2026, 10, 7)
    """

    if output_type not in ('txt', 'html'):
        return None

    if year < 1:
        return None

    if first_month not in range(1, 13) or last_month not in range(1, 13):
        return None

    if first_month > last_month:
        return None

    final_calendar = ''
    if output_type == 'txt':
        for month_idx in range(first_month, last_month + 1):
            final_calendar += TextCalendar().formatmonth(year, month_idx)
    if output_type == 'html':
        for month_idx in range(first_month, last_month + 1):
            final_calendar += HTMLCalendar().formatmonth(year, month_idx)

    return final_calendar


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
