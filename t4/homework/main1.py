n = int(input()) % 26

current_ord = ord('A')
last_ord = current_ord + n

# спосіб 1. сума
# сума гаус (1+k)/2 * k = sum 1 2 3 4 5 ... k
n_lines_sum = 1
while (n_lines_sum + 1) / 2 * n_lines_sum < n:
    n_lines_sum += 1

print(f'sum --> {n_lines_sum}')

# спосіб 2. цикл
n_lines = 1
n_nums = n
for i in range(1, 7): # 7 : 22-29
    if (n_nums := n_nums - i) <= 0:
        break
    n_lines += 1

print(n_lines)

print('-' * 5 + '\n')

# try printing with :.f formatting !! 10 symbs allocated for ex

for i in range(1, n_lines + 1):
    print('  ' * (n_lines - i), end='')
    end_ord = current_ord + i
    end_ord = end_ord if end_ord <= last_ord else last_ord
    while current_ord < end_ord:
        print(chr(current_ord) + ' ' * (current_ord < end_ord - 1), end='')
        current_ord += 1

    print()
