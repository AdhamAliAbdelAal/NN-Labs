import numpy as np
x=np.array([1,2,3])
x=x.reshape(-1,1)
y=np.array([
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ])

print(y-x)

t=0
t+=x
print(t)
t+=t
print(t)