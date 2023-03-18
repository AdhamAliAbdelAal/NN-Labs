import numpy as np

# x= np.array([
#     [1,2,3],
#     [4,5,6],
# ])


# y =x[x[:,0]==1]
# y=np.mean(x,axis=0)
# y = np.array([
#     [1,2,3],
# ])



# x= np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# y= np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12],
# ])

# # x= np.array([1,2,3])
# # y= np.array([1,2,3,4])
# print(y-x[:,np.newaxis])

# print(x[:,np.newaxis].shape,y.shape)

# z= np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [10,20],
#         [30,40]
#     ]
# ])
# print(np.transpose(z,(0,2,1)))

# x= np.array([
#     [1,2],
#     [3,4],
#     [5,6]
# ])

# y= np.array([1,2])

# print(y-x)

# # three dimensional arrays
# m1 = np.array([[1, 6, 5],[3 ,4, 8],[2, 12, 3]]) 
# m2 = np.array([[3, 4, 6],[5, 6, 7],[6,56, 7]]) 
# m3 = np.dot(m1,m2) 


# print(m3) 

x= np.array([
    [
    [1,2],
    [3,4],
    ],
    [
    [1,2],
    [3,4],
    ],
    ])

y= np.array([
    [1,2],
    [3,4],
])

print(np.dot(x,y))


x=np.array([
    [1,2,3],
    [1,2,4]
])

y=np.array([1,2,3])

print(np.dot(x,y))

x= np.array([
    [
    [1,2],
    [3,4],
    ],
    [
    [1,2],
    [3,4],
    ],
    [
    [1,2],
    [3,4],
    ]
    ])
y=np.array([
    [1,2],
    [3,4],
    [5,6]
])
y=y[:,:,np.newaxis]
print(y)
print(y.shape,x.shape)
print(1/(np.transpose(y,(0,2,1))@x@y))
#print(np.dot(x,y.T))

# x=np.ones((3,3))
# y=np.array([[1,2,3]])
# print(np.dot(y,x))
