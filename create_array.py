# create_array.py

import numpy as np

a = np.array([1, 2, 3])
b = np.array([(1,2,3), (4,5,6)])

print('a=')
print(a)
print("a's ndim {}".format(a.ndim))
print("a's shape {}".format(a.shape))
print("a's size {}".format(a.size))
print("a's dtype {}".format(a.dtype))
print("a's itemsize {}".format(a.itemsize))

print('')

print('b=')
print(b)
print("b's ndim {}".format(b.ndim))
print("b's shape {}".format(b.shape))
print("b's size {}".format(b.size))
print("b's dtype {}".format(b.dtype))
print("b's itemsize {}".format(b.itemsize))

