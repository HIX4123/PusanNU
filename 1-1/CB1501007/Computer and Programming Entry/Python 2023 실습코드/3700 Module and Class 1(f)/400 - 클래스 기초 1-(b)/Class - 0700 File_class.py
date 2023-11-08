
class SeqFile:
        def __init__(self, fname):
                self.f = open(fname)
        def __getitem__(self, k):
                line = self.f.readline()
                if not line: raise IndexError(k)
                return self.filter(line)   # ?닿? ?먰븯???꾪꽣 ?곸슜
        def filter(self, line):  # ?꾪꽣 ?뺤쓽
                return line.rstrip()  # ?ㅼ쓽 怨듬갚???놁븻??

s2 = SeqFile('t.txt')
for line in s2:
        print(line, end=' ')
