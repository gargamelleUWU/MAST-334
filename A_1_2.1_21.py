import sympy as sp
import utils

# setting up the mathematical variable and the function
x = sp.Symbol('x')
func = sp.sin(sp.pi*x)

# Applying the bisection method to find the root of the function in different intervals
utils.bisect(func, x, -0.2, 2.1, 10**-4)

utils.bisect(func, x, -0.1, 2.9, 10**-4)

utils.bisect(func, x, -0.5, 2.5, 10**-4)