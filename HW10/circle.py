import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
center_x = -40
center_y = 40
inner_r = 20.0
outter_r = 60.0
background = np.array([0, 0, 0, 0])
# background = np.expand_dims(background, axis=(0, 1))

color = np.array([1.0, 1.0, 0.0, 0.8]) # (R, G, B, A)
# color = np.expand_dims(color, axis=(0, 1))
print(color.shape)
Y, X = np.mgrid[-128:128, -128:128]


# X = np.expand_dims(X, axis=0) 
# X = np.tile(X, reps=(4, 1))
# Y = np.expand_dims(Y, axis=0) 
# Y = np.tile(Y, reps=(4, 1))

cond_1 = inner_r**2 <= ((X - center_x)**2 + (Y - center_y)**2)
cond_2 = ((X - center_x)**2 + (Y - center_y)**2) <= outter_r**2
q = np.where(np.expand_dims(np.logical_and(cond_1, cond_2), axis=-1), color, background)
print(q.shape)
plt.imshow(q)

plt.show()
# I = ??? # Maybe you need several expressions
# Print(I.shape) # (256, 256, 4)
# # it means 256x256 pixels of (R, G, B, A) 
# # background = img.imread('data/landscape.jpg')
# # plt.imshow(background)
# plt.imshow(I)
# plt.show()