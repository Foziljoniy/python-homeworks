
import numpy as np

# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# Create a 3x3x3 array with random values
array_3x3x3 = np.random.random((3, 3, 3))

# Create a 10x10 array with random values and find the minimum and maximum values
array_10x10 = np.random.random((10, 10))
min_val, max_val = np.min(array_10x10), np.max(array_10x10)

# Create a random vector of size 30 and find the mean value
vector_30 = np.random.random(30)
mean_val = np.mean(vector_30)

# Normalize a 5x5 random matrix
matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - np.min(matrix_5x5)) / (np.max(matrix_5x5) - np.min(matrix_5x5))

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product = np.dot(matrix_5x3, matrix_3x2)

# Create two 3x3 matrices and compute their dot product
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product = np.dot(matrix_A, matrix_B)

# Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = np.transpose(matrix_4x4)

# Create a 3x3 matrix and calculate its determinant
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)

# Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B )
A = np.random.random((3, 4))
B = np.random.random((4, 3))
matrix_AB_product = np.dot(A, B)

# Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix_3x3_vec = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_vec, vector_3x1)

# Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
x_solution = np.linalg.solve(A_system, b_system)

# Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix_5x5_sum = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5_sum, axis=1)
column_sums = np.sum(matrix_5x5_sum, axis=0)

# Output results
(vector, matrix_3x3, identity_matrix, array_3x3x3, min_val, max_val, mean_val, 
 normalized_matrix, matrix_product, dot_product, transpose_matrix, determinant, 
 matrix_AB_product, matrix_vector_product, x_solution, row_sums, column_sums)
