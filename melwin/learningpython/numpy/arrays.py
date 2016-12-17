import numpy as np

# every element of the array
# should be of the same type
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

print(a + b)
print(a * b)
print(a ** b)

# # len(array) v array.size
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("len(c)", len(c))
print("c.size", c.size)
