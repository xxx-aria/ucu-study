from math import sqrt, cbrt

a = float(input())
b = float(input())
c = float(input())
d = float(input())

part1 = -b ** 3 / (27 * a ** 3) + b * c / (6 * a ** 2) - d / (2 * a)
part2 = c / (3 * a) - b ** 2 / (9 * a ** 2)
sqrt_part = sqrt(part1 ** 2 + part2 ** 3)

x = cbrt(part1 + sqrt_part) + cbrt(part1 - sqrt_part) - b / (3 * a)

print(f'{x = :.2f}')
