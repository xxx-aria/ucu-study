n = int(input())

current_ord = ord('A')
last_ord = current_ord - 1 + n

n_lines = 0
n_nums = n

# For max of 26 symbols, 7 lines is the limit
# print(sum(range(1, 8))) # 28
for i in range(7):
    if (n_nums := n_nums - i) <= 0:
        break
    n_lines += 1

for i in range(1, n_lines + 1):
    print('  ' * (n_lines - i), end='')

    for j in range(i):
        if current_ord == last_ord:
            print(chr(current_ord), end='')
            break
        print(chr(current_ord), end=' ' * (j != i - 1))
        current_ord += 1

    print()
