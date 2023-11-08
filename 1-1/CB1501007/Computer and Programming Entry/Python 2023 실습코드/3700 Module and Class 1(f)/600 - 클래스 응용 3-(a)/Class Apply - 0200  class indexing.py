
# class12.py

class Square:
        def __init__(self, end):
                self.end = end
        def __len__(self):
                return self.end
        def __getitem__(self, k):
                if type(k) == type(0): # indexing
                        if k < 0 or self.end <= k: raise IndexError(k)
                        return k * k
                else:  # slicing
                        start = k.start or 0
                        if k.stop > self.end: stop = self.end
                        else: stop = k.stop
                        step = k.step or 1
                        return list(map(self.__getitem__, list(range(start, stop, step))))


s = Square(10)
print(s[4])      #
print(s[1:5])    #
print(s[1:10:2])   #
print(s[:])        #
