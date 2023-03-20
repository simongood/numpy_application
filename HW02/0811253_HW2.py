def add0(x):
    return'000' + str(x)
def addY(x):
    return'Y' + str(x)
L = [1, 10, 12, 2, 3, 320, 506]

M = list(map(add0, L))
L = list(map(lambda x: x[-len(str(max(L))):], M))
N = list(map(addY, L))
print(N)