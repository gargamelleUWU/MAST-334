import sympy as sp

# Setting up the mathematical variable and the function
x = sp.Symbol('x')
f = (sp.exp(x)-sp.exp(-x)) / x

# Part a: Finding the limit of f(x) as x approaches 0
f_limit =sp.limit(f, x, 0)
print("Part A")
print(f"Limit of f(x) as x approaches 0 = {f_limit}")

# Part b: Evaluating f(0.1) and rounding to 3 decimal places
# Unsure if I should evaluate each individual portion to the third digit or evaluate the entire expression and then round to 3 digits. I will do the former for now.
exp_pos = sp.exp(0.1).evalf(3)
exp_neg = sp.exp(-0.1).evalf(3)
three_digit_evaluation = (exp_pos - exp_neg) / 0.1
print("Part B")
print(f"f(0.1) rounded to 3 decimal places = {three_digit_evaluation.evalf(3)}")

# Part c: evaluation P3(0.1) and rounding to 3 decimal places
mac_1 = sp.exp(x).series(x, 0, 4).removeO()
mac_2 = sp.exp(-x).series(x, 0, 4).removeO()
f_approx = (mac_1 - mac_2) / x
three_digit_approximation = f_approx.subs(x, 0.1).evalf(3) # Unsure if I should round to 3 decimals or 3 significant figures
print("Part C")
print(f"P3(0.1) rounded to 3 decimal places = {three_digit_approximation}")


# Part d: Find the relative error between f(0.1) and the results of part (b) and part (c)
accurate_value = f.subs(x, 0.1).evalf()
relative_error_b = abs((accurate_value - three_digit_evaluation) / accurate_value)
relative_error_c = abs((accurate_value - three_digit_approximation) / accurate_value)
print("Part D")
print(f"Relative error between f(0.1) and part (b) = {relative_error_b}")
print(f"Relative error between f(0.1) and part (c) = {relative_error_c}")