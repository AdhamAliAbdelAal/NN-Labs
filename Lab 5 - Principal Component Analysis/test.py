import numpy as np

x=np.array([
    [1,2,3],
    [4,5,6],
           ])
print(np.mean(x,axis=0))

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
