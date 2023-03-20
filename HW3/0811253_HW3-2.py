class student:
    def __init__(self, id='00', name='none', age=0, score=[0.0, 0.0, 0.0]):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'ID: ' + self.id + '\n' \
               + 'Name: ' + self.name + '\n' \
               + 'Age: ' + str(self.age) + '\n' \
               + 'score : ' + str(self.score) + '\n' \
               + '.......................' + '\n'

    def __repr__(self):
        return self.__str__()

class SortKey:
    def __init__(self, m=0):
        if m == 0:
            self.m = 0
        elif m == 1:
            self.m = 1
        else:
            self.m = m


    def __call__(self, x):
        return x.score[self.m]

Mary = student('A000', 'Mary', 20, [90, 80, 75])
James = student('A010', 'James', 20, [82, 60, 91])
Ann = student('A008', 'Ann', 19, [95, 92, 100])
Tim = student('A208', 'Tim', 21, [56, 72, 50])

print('----------original-------------')
L = [Mary, James, Ann, Tim]
print(L)

print('------Sorting by score[0]------')
L.sort(key = SortKey(0))
print(L)

print('------Sorting by score[1]------')
L.sort(key = SortKey(1))
print(L)

print('------Sorting by score[2]------')
L.sort(key = SortKey(2))
print(L)