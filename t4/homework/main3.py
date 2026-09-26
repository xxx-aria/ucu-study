# ...###...
START_BALANCE = 15

balance = START_BALANCE
skyscraper = ''
prev_block = ''
res_count = 0

while balance > 0:
    block = input()

    res_count += 1

    if skyscraper:
        skyscraper += '\n'
    skyscraper += block

    print('-' * 5)
    print('\tur scyscraper:')
    print(skyscraper)


    if not prev_block: # first el
        print(f'{balance = }')
        print('-' * 5)
        prev_block = block
        continue

    if block == prev_block:
        print(f'{balance = }')
        print('-' * 5)
        continue

    # NICE IDEA !!
    # catching first # and evaluating ### positions
    counter = 0
    prev_counter = 0
    for symbol in block:
        counter += 1
        if symbol == '.':
            continue
        print(f'\tfound # in this on {counter}')
        for prev_symbol in prev_block:
            prev_counter += 1
            if prev_symbol == '.':
                continue
            print(f'\tfound # in prev on {prev_counter}')
            difference = abs(counter - prev_counter)
            print(f'\tdiff is {difference}')
            # no case for 0, eliminated with == earlier
            if difference == 1:
                balance -= 1
            elif difference == 2:
                balance -= 2
            else: # new skycraper!! distance btwn # >= 3
                balance -= 3
                block = prev_block
                res_count -= 1
            break
        break

    print(f'{balance = }')
    print('-' * 5)

    prev_block = block

print('\n\n\n' + '-' * 10)
print(res_count)
print(skyscraper)
