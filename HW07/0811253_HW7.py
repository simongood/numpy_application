import numpy as np
import matplotlib.pyplot as plt

print('-----Exercise (1/3)--------')
print('---------Q1-----------')
images = 10
channels = 3
height = 200
width = 100
A = np.full((images, channels, height, width), 0.2)
A[:, 1, ...] = 0.3
A[:, 2, ...] = 0.5
print('A[0][0][150][0] = ', A[0][0][150][0])
print('(A[0][1][150][1] = ', A[0][1][150][1])
print('A[0][2][150][2]= ', A[0][2][150][2])

print('-----Exercise (2/3)--------')
pixels = height * width
B = np.reshape(A, (images, channels, pixels))
print('B.shape = ', B.shape)

C = B[2, 0, ...]
print('C.shape = ', C.shape)

D = np.reshape(C, (1, height, width))
print('D.shape = ', D.shape)

print('-----Exercise (3/3)--------')
E = np.moveaxis(A, 1, 3)
print(E.shape)
plt.imshow(E[0])
plt.show()
