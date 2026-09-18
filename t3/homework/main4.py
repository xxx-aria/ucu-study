n = int(input())


for i in range(n):
    numerator = i * 2 + 1
    denominator = numerator + 1

    match i:
        case 0:
            sign = ''
        case i if i % 2 == 0:
            sign = ' + '
        case i if i % 2 == 1:
            sign = ' - '

    print(f'{sign}{numerator}/{denominator}', end='')

print()

print('\n\t---\n')

for i in range(n):
    numerator = i * 2 + 1
    denominator = numerator + 1

    if i == 0:
        sign = ''
    elif i % 2 == 0:
        sign = ' + '
    else:
        sign = ' - '

    print(f'{sign}{numerator}/{denominator}', end='')

print()

print('\n\t---\n')

sign = '-'
for el in range(1, n * 2, 2):
    print(f'{el}/{el + 1}', end='')
    if el != n * 2 - 1:
        print(f' {sign} ', end='')
        sign = '+' if sign == '-' else '-'

print()
