import sympy as sp
from sympy import symbols, Interval
from sympy.calculus.util import minimum
import math
import utils

x = sp.Symbol('x')
g = lambda x : 2**-x
g_x = 2**-x
interval = Interval(1/3, 1)
a = 1/3
b = 1
tolerance = 10**-4

# Applying Fixed Point Iteration
accurate_iteration = utils.fix_point_iteration(g, [a, b], tolerance)

# Finding the derivative of our function g(x)
g_prime = sp.diff(g_x)

# Finding the minial value of g'(x) on interval [1/3, 1]
k = abs(minimum(g_prime, x, interval).evalf())

p0 = (a + b) / 2
p1 = g(p0)

# Estimating using inequality 2.5
max_dist = max(p0 - a, b - p0)
n = math.log(tolerance / max_dist) / math.log(k)
est_n = math.ceil(n)

# Estimating using inequality 2.6
m = math.log((tolerance * (1 - k)) / abs(p1 - p0)) / math.log(k)
est_m = math.ceil(m)


print(f"According to Inequality 2.5 the maximum number of iterations needed is {est_n}")
print(f"According to Inequality 2.6 the maximum number of iterations needed is {est_m}")