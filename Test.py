import numpy as np

#Defining the coefficients of the matrix
coeffs = [1, 3, 2, 1]

#Finding roots (poles) of the characteristic equation
roots = np.roots(coeffs)

#printing the poles of the system
print("Poles of the system:")
for pole in roots:
    print(pole)

    #Defining the matrix
    # A = [0 1 0]
    #     [0 0 1]
    #     [-1 -2 -3]
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [-1, -2, -3]])

# To get eigenvalues of matrix A
eigenvalues = np.linalg.eigvals(A)
print("Eigenvalues of matrix A:")
print(eigenvalues)