class point:
    def __init__(self,name = 'none', x=0, y=0, z=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        temp = point(self.name, self.x, self.y, self.z)
        if type(other) == float:
            temp.name += ' + ' + str(other)
            temp.x += other
            temp.y += other
            temp.z += other
        else:
            temp.name += ' + ' + str(other.name)
            temp.x += other.x
            temp.y += other.y
            temp.z += other.z
        return temp

    def __sub__(self, other):
        temp = point(self.name, self.x, self.y, self.z)
        if type(other) == float:
            temp.name += ' - ' + str(other)
            temp.x -= other
            temp.y -= other
            temp.z -= other
        else:
            temp.name += ' - ' + str(other.name)
            temp.x -= other.x
            temp.y -= other.y
            temp.z -= other.z
        return temp

    def __mul__(self, other):
        temp = point(self.name, self.x, self.y, self.z)
        if type(other) == float:
            temp.name += ' * ' + str(other)
            temp.x *= other
            temp.y *= other
            temp.z *= other
        else:
            temp.name += ' * ' + str(other.name)
            temp.x *= other.x
            temp.y *= other.y
            temp.z *= other.z
        return temp

    def __str__(self):
        return self.name + ' = (' + str(self.x) + ', '+ str(self.y) + ', ' + str(self.z) + ')'

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        return self.x*(1/self.length()), self.y*(1/self.length()), self.z*(1/self.length())

p1 = point('p1', 1, 2, 3)
p2 = point('p2', 4, 5, 6)
w = 5.0
p3 = p1 + p2



print(p1 + p2)
print(p1 - p2)
print(p1 + w)
print(p1 - w)
print(p1 * w)
print(p1 * p2)
print('(p1)length = ', p1.length())
print('(p1)normalize = ', p1.normalize())

