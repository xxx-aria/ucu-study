# ...###...
START_BALANCE = 15

balance = START_BALANCE
prev_pos = -1
total_height = 0

while balance > 0:
    block = input()
    total_height += 1

    # catching first # position
    curr_pos = 0
    for symbol in block:
        if symbol == '#':
            break
        curr_pos += 1

    if prev_pos == -1: # for the first block
        prev_pos = curr_pos
        continue

    difference = abs(prev_pos - curr_pos)
    match difference:
        case 0:
            pass
        case 1:
            balance -= 1
        case 2:
            balance -= 2
        case _: # difference >= 3
            balance -= 3
            curr_pos = prev_pos
            total_height -= 1

    prev_pos = curr_pos

print(total_height)
