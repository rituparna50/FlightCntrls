import sympy as sp

#Defining desired overshoot
desired_overshoot = 10

# Assuming damping ratio
zeta = 0.7

# Defining desired overshoot in decimal form
desired_overshoot_decimal = desired_overshoot / 100

# Declare symbolic variable s
s = sp.symbols('s')

# Define the closed-loop transfer function equation
G = sp.simplify(sp.Poly(1 / (s**2 + 2 * zeta * s + 1)).as_expr())

# Define the second-order transfer function equation with overshoot
G_overshoot = sp.simplify(sp.Poly(1 / (1 - desired_overshoot_decimal)).as_expr())

# Solve the equation to find the gain 'K'
solutions = sp.solve(sp.Eq(G, G_overshoot), sp.symbols('K'))

# Print the value of 'K'
for solution in solutions:
    if solution.is_real:
        K = solution.evalf()
        print("Gain value (K):", K)