import numpy as np

x=np.array([
    [1,2,3,4,5,7],
    [3,4,5,6,7,8],
    [5,6,7,8,9,10],
    [7,8,9,10,11,12],
    [9,10,11,12,13,14],
    [11,12,13,14,15,16],
        ])
u=np.array([
    [10,20],
    [30,40],
])
y=np.array([
    1,3,4
])
print(x[:,y])

def projectData(X, U, K):
    U= U[:K,:]
    Z = U[np.newaxis,:,:]@X[:,:,np.newaxis]
    return Z.reshape(-1,1)


# print(projectData(x,u,1))
# print(np.flip(x,axis=1))

# print(np.cov(x,rowvar=False))

# x=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ])
# w,v = np.linalg.eigh(x)
# print(w)
# print(v)
# print(np.flip(x,axis=0))

# x=np.array([
#     [1,2],
# ])

# y=np.array([
#     [3,4],
#     [5,6],
#     [7,8],
#     [9,10],
#     [11,12],
# ])

# print(x[np.newaxis,:,:].shape)
# x=x[np.newaxis,:,:]
# print(y[:,:,np.newaxis].shape)
# y=y[:,:,np.newaxis]
# print("***********")
# print((x@y))
