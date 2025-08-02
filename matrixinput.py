import numpy as np

def input_matrix(name):
    print(f"\nEnter the dimensions of Matrix {name}:")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    
    print(f"Enter the elements of Matrix {name} row-wise (separated by space):")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid number of elements. Please try again.")
            return input_matrix(name)
        elements.append(row)
    
    return np.array(elements)

# Input matrices
A = input_matrix("A")
B = input_matrix("B")

# Check shape compatibility for basic operations
if A.shape != B.shape:
    print("\nMatrix addition, subtraction, and element-wise multiplication require matrices of the same shape.")
else:
    # Addition
    print("\nMatrix Addition:\n", A + B)

    # Subtraction
    print("\nMatrix Subtraction:\n", A - B)

    # Element-wise Product
    print("\nElement-wise Product (Hadamard):\n", A * B)

# Matrix multiplication (dot product)
try:
    multiplication = np.dot(A, B)
    print("\nMatrix Multiplication (Dot Product):\n", multiplication)
except ValueError:
    print("\nMatrix multiplication not possible due to incompatible shapes.")

# Rank
print("\nRank of Matrix A:", np.linalg.matrix_rank(A))

# Inverse
if A.shape[0] == A.shape[1]:
    try:
        inverse_A = np.linalg.inv(A)
        print("\nInverse of Matrix A:\n", inverse_A)
    except np.linalg.LinAlgError:
        print("\nMatrix A is singular and cannot be inverted.")
else:
    print("\nMatrix A is not square, so inverse is not defined.")
