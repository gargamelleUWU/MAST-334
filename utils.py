import sympy as sp

# Bisection function to find the root of a function within a given interval [a, b] with a specified tolerance TOL.
def bisect(f, symbol, a, b, TOL):
    f_num = sp.lambdify(symbol, f)

    fa = f_num(a)
    fb = f_num(b)


    if fa * fb >= 0:
        print(f"Cannot Guarantee a root in the interval [{a}, {b}]")

    c = a
    while (b - a) >= TOL:
        c = (a + b) / 2
        fc = f_num(c)
        if abs(fc) < TOL:
            break

        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
            
    print(f"The root is approximately at x = {c:.5f})")

# Convergence iteration function to evaluate the convergence rate.
def convergence_iteration(func, initial_guess, iterations, target, tolerance):
    current_value = initial_guess
    for i in range(iterations):
        try:
            current_value = func(current_value)
            print(f"Iteration {i+1}: {current_value}")

            if abs(current_value - target) < tolerance:
                print(f"Formula converged in {i+1} steps")
                return i + 1

        except OverflowError:
            print(f"Formula divereged, value exploded to infinity:")
            return None
        except Exception as e:
            print(f"Unexpected error at iteration {i+1}: {e}")
            return None

    print(f"Did not converge within {iterations} iterations. Last value: {current_value}")
    return None