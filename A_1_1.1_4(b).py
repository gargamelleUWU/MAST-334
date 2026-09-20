import sympy as sp

# Setting up the mathematical variable and the function
x = sp.Symbol('x')
f = 4*x**2 - sp.exp(x)

# iterating through the defined range to find the intervals where the function changes sign
# The sign change guarantees a root in that interval
for i in range(-5, 6):
    a = i
    b = i + 1

    # evaluating f(i) and f(i+1) to check for sign change.
    f_a = f.subs(x, a).evalf()
    f_b = f.subs(x, b).evalf()

    # printing the results
    if f_a * f_b < 0:
        print(f"Root exists in the interval [{a}, {b}]")