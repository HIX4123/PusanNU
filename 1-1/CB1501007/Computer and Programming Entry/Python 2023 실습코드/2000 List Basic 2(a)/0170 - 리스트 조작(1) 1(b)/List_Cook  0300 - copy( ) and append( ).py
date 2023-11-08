
import copy

la = [ 1,2,3,4,5]
lb = copy.copy(la)
la.append(100)

print la
print lb

La= [[]]
Lb= [[6]]

La.extend(Lb)
print La

lc=[ [1,2], [1,3], [1,4]]

ld= copy.copy(lc)
lc.append(3)

print lc
print ld