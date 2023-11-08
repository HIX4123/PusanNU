
def f1(seq):  # not order preserving
   set = {}
   list(map(set.__setitem__, seq, []))
   return list(set.keys())

def f2(seq): # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

def f3(seq):    # Not order preserving
   keys = {}
   for e in seq:
       keys[e] = 1
   return list(keys.keys())

def f4(seq):    # order preserving
   noDupes = []
   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   return noDupes

def f5(seq, idfun=None):    # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item) # in old Python versions:  if seen.has_key(marker)  but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def f6(seq): # Not order preserving
   lset = set(seq)
   return list(lset)


A= [10, 10, 1, 2, 3, 3, 4, 5, 7, 9, 10]

print(f6(A))
print(f5(A))

a= list('abccABBCDcdffffza')
print(f5(a))
print(f5(a, lambda x: x.lower()))     # 대소문자를 같이 보고 같으면 지운다.


