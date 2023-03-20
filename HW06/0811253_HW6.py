import matplotlib.pyplot as plt

def quadratic(X, A):  # A= [c, b, a] [0次方, 1次方, 2次方]
    L = []
    for i in range(len(X)):
        L.append(A[0] + A[1]*X[i] + A[2]*X[i]**2)
    return L

A1 = [1, 2, 3]
A2 = [-1, -2, -3]
A3 = [4, 5, 6]
X1 = []
Y1 = []
Y2 = []
Y3 = []
# total
X = []
Y = []

for i in range(100):
    X1.append(-0.5 + i/100)
Y1 = quadratic(X1, A1)
Y2 = quadratic(X1, A2)
Y3 = quadratic(X1, A3)

for i in range(100):
    X.append([X1[i]]*3)
    Y.append([Y1[i], Y2[i], Y3[i]])

print(X)
print(Y)


plt.gca().set_prop_cycle('color', ['red', 'blue', 'green', 'black'])
plt.plot(X, Y, 'r')
plt.plot(X, Y, linestyle='solid', linewidth=5)
plt.savefig('fig.png')





