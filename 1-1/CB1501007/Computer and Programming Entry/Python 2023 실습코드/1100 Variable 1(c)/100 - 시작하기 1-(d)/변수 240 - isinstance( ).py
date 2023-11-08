
L=[]
L.append( isinstance(1, int))
L.append( isinstance(1.2, float))
L.append( isinstance(1.2, int))
L.append( isinstance("hi", str))
mylist=[]
L.append( isinstance(mylist, list))

for (i,w) in enumerate(L) :
    print(f"i={i}, {w}" )


M = [ 3.45, 90, 0.234, "Good", [3,4,5], -0.98]
for w in M :
    if isinstance(w, float) :
        print(w)


