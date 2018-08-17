class Range():
    '''
    This class is to implement the main function of the built-in range, and it now supports
    iteration and select by using minus numbers
    '''
    def __init__(self,start,stop=None,step=1):
        if step == 0:
            raise ValueError('step couldn\'t be zero !')

        if stop is None:
            if step > 0:
                start, stop = 0 , start
            else:
                start, stop = start , 0
        self._start = start
        self._stop = stop
        self._step = step
        step = abs(step)
        self._length = max(0, abs((stop - start + step - 1) //  step))
        self._k = -1

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < len(self):
            raise IndexError('index out of range')
        return self._start + k*self._step

    def __next__(self):
        self._k += 1
        if(self._k < len(self)):
            return self[self._k]
        else:
            self._k = -1
            raise StopIteration()

    def __iter__(self):
        return self

    def __str__(self):
        data = []
        for i in self:
            data.append(i)
        return ('<' + str(data)[1:-1] + '>')



r = Range(5,1,-2)
print(r)
for i in (range(5,1,-2)):
    print(i)
