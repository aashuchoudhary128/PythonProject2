import numpy as np
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
addition = matrix1 + matrix2
print("\nMatrix Addition Result:\n", addition)
multiplication = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        for k in range(3):
            multiplication[i][j] += matrix1[i][k] * matrix2[k][j]
print("\nMatrix Multiplication Result:\n", multiplication)