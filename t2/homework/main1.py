from math import pi, sqrt, exp

x = float(input())
mu = float(input())
sigma = float(input())

result = 1 / sqrt(2 * pi * sigma ** 2) * exp(-(x - mu) ** 2 / (2 * sigma ** 2))
print(f'{result:.10f}')
