import numpy as np
matrix1=np.array([[71,41],
                 [41,62]])

matrix2=np.array([[45],
                  [125]])
x=np.linalg.solve(matrix1,matrix2)
print("the solution ",x)

