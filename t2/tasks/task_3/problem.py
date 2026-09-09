from math import cosh, exp, e

x = float(input())

cosh_lib = cosh(x)
cosh_exp = (exp(x) + exp(-x)) / 2
cosh_e = (e ** x + e ** -x) / 2

print(f'{cosh_lib = :.4f}\n{cosh_exp = :.4f}\n{cosh_e = :.4f}')
