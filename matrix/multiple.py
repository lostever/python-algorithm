from numpy import *

a = array(([1,2,3],
            [4,5,6],
            [7,8,9]))

b = array(([7,8],
            [9,10],
            [11,12]))

a = mat(a)
b = mat(b)

print(a*b)