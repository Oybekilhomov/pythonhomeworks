##num1

import numpy as np

vector = np.arange(10, 50)
print(vector)


##num2

import numpy as np

matrix = np.arange(9).reshape(3, 3)
print(matrix)


##num3

import numpy as np

identity_matrix = np.eye(3)
print(identity_matrix)


##num4

import numpy as np

array = np.random.rand(3, 3, 3)
print(array)


##num5

import numpy as np

array = np.random.rand(10, 10)
min_val = array.min()
max_val = array.max()

print("Minimum value:", min_val)
print("Maximum value:", max_val)


##num6

import numpy as np

vector = np.random.rand(30)
mean_val = vector.mean()

print("Mean value:", mean_val)


##num7

import numpy as np

matrix = np.random.rand(5, 5)
normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print("Normalized matrix:\n", normalized)


##num8

import numpy as np

A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
product = np.dot(A, B)

print("Product matrix (5x2):\n", product)


##num9

import numpy as np

A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
dot_product = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Dot product (A · B):\n", dot_product)


##num10

import numpy as np

matrix = np.random.rand(4, 4)
transpose = matrix.T

print("Original matrix:\n", matrix)
print("Transposed matrix:\n", transpose)


##num11

import numpy as np

matrix = np.random.rand(3, 3)
determinant = np.linalg.det(matrix)

print("Matrix:\n", matrix)
print("Determinant:", determinant)


##num12

import numpy as np

A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
product = np.dot(A, B)

print("Matrix A (3x4):\n", A)
print("Matrix B (4x3):\n", B)
print("Matrix Product A · B (3x3):\n", product)


##num13

import numpy as np

matrix = np.random.rand(3, 3)

vector = np.random.rand(3, 1)

product = np.dot(matrix, vector)

print("Matrix (3x3):\n", matrix)
print("Vector (3x1):\n", vector)
print("Matrix-Vector Product:\n", product)


##num14

import numpy as np

A = np.random.rand(3, 3)
b = np.random.rand(3, 1)

x = np.linalg.solve(A, b)

print("Matrix A:\n", A)
print("Vector b:\n", b)
print("Solution x:\n", x)


##num15

import numpy as np

matrix = np.random.rand(5, 5)

row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)

print("Matrix:\n", matrix)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)

