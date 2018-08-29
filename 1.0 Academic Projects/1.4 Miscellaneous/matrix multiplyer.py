"""Matrix multiplyer"""

import numpy as np 

X=[[1,2,3],[4,5,6],[7,8,9]]

Y=[[1,2,3],[4,5,6],[7,8,9]]

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print result
