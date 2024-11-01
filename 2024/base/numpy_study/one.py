import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)

identity_matrix = np.eye(3)
identity_matrix
print(identity_matrix)

coefficients = np.array([[4, 5], [7, 8]])
dependent_values = np.array([32, 50])
solution = np.linalg.solve(coefficients, dependent_values)
print(solution)

product = np.dot(coefficients, solution)
print(product)
