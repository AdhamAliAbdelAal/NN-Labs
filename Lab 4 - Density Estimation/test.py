import numpy as np

x=np.array([
    [1,2],
    [3,4],
    [1,6],
    [1,8],
])

print(x[x[:,0]==1][:,1])
x=np.array([
    1,2,3
])

y=np.array([
    1,2
])
print(x[:,np.newaxis])
print(x[:,np.newaxis]-y)