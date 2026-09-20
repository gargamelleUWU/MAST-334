import sympy as sp
import utils

x = sp.Symbol('x')
func = x**2 - 3
digits = 10**-4

utils.bisect(func, x, 0, 10, digits)