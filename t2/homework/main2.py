from math import sqrt, cbrt

a = float(input())
b = float(input())
c = float(input())
d = float(input())

f1 = - b ** 3 / (27 * a ** 3) + b * c / (6 * a ** 2) - d / (2 * a)
f2 = c / (3 * a) - b ** 2/ (9 * a ** 2)

x = cbrt(f1 + sqrt(f1 ** 2 + f2 ** 2)) + cbrt(f1 - sqrt(f1 ** 2 + f2)) - b / (3 * a)
print(f'{x = :.2f}')
