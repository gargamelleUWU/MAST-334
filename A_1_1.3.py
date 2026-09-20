import sympy as sp

# setting up the mathematical variable
n = sp.Symbol('n')
sequence = (sp.ln(n+1)-sp.ln(n))
squence_limit = sp.limit(sequence, n, sp.oo)
print(f"Limit of the sequence as n approaches infinity = {squence_limit}")

error = abs(squence_limit - sequence)

for p in range(1,6):
    beta_n = 1 / n**p
    ratio_limit = sp.limit(error / beta_n, n, sp.oo)
    if ratio_limit != 0 and ratio_limit != sp.oo:
        print(f"The Sequence converges with rate O(1/n^{p})")
        break

#===================================================

h = sp.Symbol('h')
func = (1 - sp.exp(h)) / h
L = -1

error_func = abs(func - L)

for p in range(1,6):
    G_h = h**p
    ratio_limit_func = sp.limit(error_func / G_h, h, 0)
    if ratio_limit_func != 0 and ratio_limit_func != sp.oo:
        print(f"The Function converges with rate O(h^{p})")
        break

