# shape_manipulation.py

import numpy as np

zero_line = np.zeros((1,3))
one_column = np.ones((3,1))
print("zero_line = \n{}\n".format(zero_line))
print("one_column = \n{}\n".format(one_column))

a = np.array([(1,2,3), (4,5,6)])
b = np.arange(11, 20)
print("a = \n{}\n".format(a))
print("b = \n{}\n".format(b))

b = b.reshape(3, -1)
print("b.reshape(3, -1) = \n{}\n".format(b))

c = np.vstack((a, b, zero_line))
print("c = np.vstack((a,b, zero_line)) = \n{}\n".format(c))

a = a.reshape(3, 2)
print("a.reshape(3, 2) = \n{}\n".format(a))

d = np.hstack((a, b, one_column))
print("d = np.hstack((a,b, one_column)) = \n{}\n".format(d))

# np.vstack((a,b)) # ValueError: dimensions not match

e = np.hsplit(d, 3) # Split a into 3
print("e = np.hsplit(d, 3) = \n{}\n".format(e))
print("e[1] = \n{}\n".format(e[1]))

# np.hsplit(d, 4) # ValueError: array split does not result in an equal division

f = np.hsplit(d, (1, 3)) # # Split a after the 1st and the 3rd column
print("f = np.hsplit(d, (1, 3)) = \n{}\n".format(f))

g = np.vsplit(d, 3)
print("np.vsplit(d, 3) = \n{}\n".format(g))

# np.vsplit(d, 2) # ValueError: array split does not result in an equal division