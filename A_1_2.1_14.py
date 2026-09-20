import sympy as sp
import utils

x = sp.Symbol('x')
func = x**2 - 3
digits = 10**-4

# Applying the bisection method to find the root of the function in different intervals
utils.bisect(func, x, 0, 10, digits)