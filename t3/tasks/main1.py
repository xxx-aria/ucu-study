for i in range(0):
    turn = input()

    if not turn:
        break

    turn_1, turn_2 = turn

    if turn_1 == turn_2:
        print('Draw')
    elif turn in ('RS', 'SP', 'PR'):
        print('True')
    elif turn in ('RP', 'SR', 'PS'):
        print('False')


for _ in range(10):
    # match turn := input():
    match input():
        case '':
            break
        case 'RR' | 'SS' | 'PP':
            print('Draw')
        case 'RS' | 'SP' | 'PR':
            print('True')
        case 'RP' | 'SR' | 'PS':
            print('False')


counter = 0
while (counter := counter - 1) >= 0 and (turn := input()):
    res = 'Draw'
    match turn:
        case 'RS' | 'SP' | 'PR':
            res = 'True'
        case 'RP' | 'SR' | 'PS':
            res = 'False'
    print(res)
