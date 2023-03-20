import numpy as np
import matplotlib.pyplot as plt

ox = np.linspace(2, 16, 8)  # original x
oy = [10, 50, 70, 75, 40, 10, 30, 35]   # original y


A = np.matrix([ox**3, ox**2, ox, [1]*8]).transpose() # 8 x 2 matrix
b = np.matrix([oy]).transpose() # 8 x 1 array
R = np.linalg.lstsq(A, b, rcond = None)
x = R[0]
print('a,b,c,d = \n',x)

x_fit = np.linspace(2, 16, 100)
A_fit = np.matrix([x_fit**3, x_fit**2, x_fit, [1]*100]).transpose()
b_fit = A_fit*x
y_fit = np.array(b_fit.transpose())
y_fit = y_fit.squeeze()

plt.plot(ox, oy, 'ro-', markersize=3)
plt.plot(x_fit, y_fit, 'b-')
plt.show()