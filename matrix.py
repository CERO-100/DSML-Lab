import numpy as np

# Define two matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. Matrix Addition
addition = A + B
print("Matrix Addition:\n", addition)

# 2. Matrix Subtraction
subtraction = A - B
print("Matrix Subtraction:\n", subtraction)

# 3. Matrix Multiplication (Dot Product)
multiplication = np.dot(A, B)
print("Matrix Multiplication (Dot Product):\n", multiplication)

# 4. Element-wise Multiplication (.product)
elementwise_product = A * B  # or use np.multiply(A, B)
print("Element-wise Product (Hadamard):\n", elementwise_product)

# 5. Rank of Matrix A
rank_A = np.linalg.matrix_rank(A)
print("Rank of Matrix A:", rank_A)

# 6. Inverse of Matrix A
try:
    inverse_A = np.linalg.inv(A)
    print("Inverse of Matrix A:\n", inverse_A)
except np.linalg.LinAlgError:
    print("Matrix A is singular and cannot be inverted.")
