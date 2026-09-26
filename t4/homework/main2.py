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
print(f'{max_volume = }')


current_volume = 0
total_volume = 0

cherries_count = 0

while True:
    command = input()

    if command == 'q':
        try:
            cherries_ratio = (cherries_count * ONE_CHERRY_VOLUME) / current_volume
        except ZeroDivisionError:
            print('\t\tempty glass')
        else:
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
        continue

    vol = 0
    count = ''
    for x in command:
        if vol == 0:
            if x == '#':
                vol = ONE_POURING_VOLUME
                continue
            elif x == '0':
                vol = ONE_CHERRY_VOLUME
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
        print(f'\t\t\ttotal cherries = {cherries_count}')

    print(f'\t\t{vol} * {count}')
    print(f'{current_volume = }, {total_volume = }')
