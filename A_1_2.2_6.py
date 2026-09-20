import sympy as sp 
import utils
p = sp.Symbol('p')

# Defining the functions for each equation
pa = lambda p: p * (1 + ((7 - p**5) / (p**2)))**3
pb = lambda p: p - ((p**5 - 7) / (p**2))
pc = lambda p: p - ((p**5 - 7) / (5 * p**4))
pd = lambda p: p - ((p**5 - 7) / (12))

p0 = 1.0
pn = 10
target = 7**(1/5)
tol = 10**-4

print("Equation A:")
utils.convergence_iteration(pa, p0, pn, target, tol)

print("\nEquation B:")
utils.convergence_iteration(pb, p0, pn, target, tol)

print("\nEquation C:")
utils.convergence_iteration(pc, p0, pn, target, tol)

print("\nEquation D:")
utils.convergence_iteration(pd, p0, pn, target, tol)