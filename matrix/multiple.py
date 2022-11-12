# from numpy import *
import numpy as np

a = np.array(([1,2], [3,4]))
b = np.array(([5,6], [7,8]))

a = np.mat(a)
b = np.mat(b)

print(a*b)