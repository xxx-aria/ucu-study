triangle_height = int(input())

for x in range(triangle_height):
    print('*' * (triangle_height - x))

print()

for i in range(1, triangle_height + 1):
    print('*' * i)

for x in range(1, triangle_height + 1):
    if x in (1, 2, triangle_height):
        print('*' * x)
        continue
    print('*' + (' ' * (x - 2)) + '*')

print('\n\n\n')

for i in range(triangle_height - 1):
    print('*' + (' ' * (i - 1)) + '*' * (i > 0))
else:
    print('*' * triangle_height)
