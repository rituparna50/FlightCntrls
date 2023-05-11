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
eigA = np.linalg.eigvals(A)
print("Eigenvalues of matrix A:")
print(eigA)


# Defining another matrix B
    B = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [-24, -26, -9]])

# To get eigen values of matrix B
    eigB = np.linalg.eigvals(B)
        print("Eigenvalues of matrix B:")
        print(eigB)