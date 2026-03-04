
import numpy as np
matrix_a = []
print("Enter elements for 5x3 matrix (3 numbers per row):")
for i in range(5):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix_a.append(row)
matrix_a = np.array(matrix_a)
matrix_b = []
print("Enter elements for 3x2 matrix (2 numbers per row):")
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix_b.append(row)
matrix_b = np.array(matrix_b)
product = np.zeros((5, 2), dtype=int)
for i in range(5):
    for j in range(2):
        for k in range(3):
            product[i][j] += matrix_a[i][k] * matrix_b[k][j]
print("\nProduct Matrix (5x2):")
print(product)