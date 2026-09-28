GLASS_VOLUME = 500
ONE_POURING_VOLUME = 20
ONE_CHERRY_VOLUME = 5

CHERRIES_MAX_RATIO = 0.15

GLASS_VOLUME_ERROR = 'Збій роботи датчика'
ALCOHOL_LIMIT_ERROR = 'Перевищено ліміт алкоголю'
CHERRIES_LIMIT_ERROR = 'Перевищено ліміт вишень'

height = float(input())
weight = float(input())
max_volume = 5 * height * weight

current_volume = 0
total_volume = 0
cherries_count = 0

while True:
    command = input()

    if command == 'q':
        if current_volume > 0:
            cherries_ratio = (cherries_count * ONE_CHERRY_VOLUME) / current_volume
            if cherries_ratio > CHERRIES_MAX_RATIO:
                print(CHERRIES_LIMIT_ERROR)
                break
        total_volume += current_volume
        print(total_volume)
        break

    if command == 'U':
        if current_volume == 0:
            continue
        if (cherries_count * ONE_CHERRY_VOLUME) / current_volume > CHERRIES_MAX_RATIO:
            print(CHERRIES_LIMIT_ERROR)
            break
        total_volume += current_volume
        current_volume = 0
        cherries_count = 0
        continue

    volume = 0
    count = ''
    for x in command:
        if x == '#':
            volume = ONE_POURING_VOLUME
            continue
        elif x == '0':
            volume = ONE_CHERRY_VOLUME
            continue

        if x == 'x':
            continue

        count += x

    try:
        count = int(count)
    except ValueError:
        count = 1
        print('invalid count')

    current_volume += vol * count

    if current_volume > GLASS_VOLUME:
        print(GLASS_VOLUME_ERROR)
        break

    if total_volume + current_volume > max_volume:
        print(ALCOHOL_LIMIT_ERROR)
        break

    if vol == ONE_CHERRY_VOLUME:
        cherries_count += count
