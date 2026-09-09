from math import pi

r = float(input())
h = float(input())

V = h * pi * (r ** 2)
A = 2 * h * pi * r + 2 * pi * (r ** 2)

print(f'{V = :.3f}')
print(f'{A = :.3f}')
