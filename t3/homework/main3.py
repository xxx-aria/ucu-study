start_num = int(input())
height = int(input())

for i in range(height, 0, -1):
    print(*range(start_num, start_num + i), sep=' ')
