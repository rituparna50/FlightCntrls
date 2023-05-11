import numpy as np

coeffs = [1, 3, -2, 1]

roots = np.roots(coeffs)
print("Poles of the system:")
for pole in roots:
    print(pole)