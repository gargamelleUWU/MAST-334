import sympy as sp

# Seting up the mathematical variable and the function
x = sp.Symbol('x')
f = x*sp.exp(x**2)

# Step 1) Computing the 4th Taloyr Polynomial P4(x)
p4 = sp.series(f, x, 0, 5).removeO()
print("The 4th Taylor Polynomial -> P4(x) =", p4)

# Part a: Upper bound for |f(x) - P4(x)| for 0 <= x <= 0.4

f_5th_derivative = sp.diff(f, x, 5)
max_5th_derivative = f_5th_derivative.subs(x, 0.4).evalf()

upper_bound = (max_5th_derivative / sp.factorial(5)) * (0.4**5)
print("Upper bound for |f(x) - P4(x)| for 0 <= x <= 0.4:", upper_bound)


# Part b: Approximate the integral on the defined bouns using P4(x)
integral_approximation = sp.integrate(p4, (x, 0, 0.4))
print("Approximate integral of f(x) from 0 to 0.4 using P4(x):", integral_approximation)

# Part c: Find the upper bound for the error in (b)
remainder_term = (max_5th_derivative / sp.factorial(5)) * (0.4**5)
integral_error_bound = remainder_term * 0.4
print("Upper bound for the error in the integral approximation:", integral_error_bound)

# Part d: Approximate f'(0.2) using P4'(0.2) and find the error
true_derivative = sp.diff(f, x).subs(x, 0.2).evalf()
p4_derivative = sp.diff(p4, x).subs(x, 0.2).evalf()
error_in_derivative = abs(true_derivative - p4_derivative)
print("True f'(0.2):", true_derivative)
print("Approximate f'(0.2) using P4'(0.2):", p4_derivative)
print("Error in the derivative approximation:", error_in_derivative)