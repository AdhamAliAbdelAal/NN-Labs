import numpy as np

x= np.array([
    [1,2,3],
    [4,5,6],
])

y =x[x[:,0]==1]
y=np.mean(x,axis=0)
print(y)