import numpy as np
x=np.array([1,2,3])
y=np.array([
    [1,2,3],
    [4,5,6],
])
print(np.linalg.norm(x-y,axis=1))
print(np.linalg.norm(x-y))