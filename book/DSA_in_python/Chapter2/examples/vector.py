class Vector():
    def __init__(self,num):
        self._coords = [0] * num
        self._k = -1

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other #it relys on the __eq__ function

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(other)):
            result[i] = self[i] + other[i]
        return result

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'  # str(self._coords) = '[string]', so we need to strip '[]' out

    def __next__(self):
        self._k += 1
        if self._k < len(self):
            return self[self._k]
        else:
            self._k = -1  # it doesn't appear in the book, but I think it's important
            raise StopIteration()

    def __iter__(self):
        return self

v = Vector(5)
print(v)

for i in v: # Though we didn't define a __next__() method at first, it implicitly works if the class has a __len__() and a __getitem()
    print(i)
for i in v:
    print(i)