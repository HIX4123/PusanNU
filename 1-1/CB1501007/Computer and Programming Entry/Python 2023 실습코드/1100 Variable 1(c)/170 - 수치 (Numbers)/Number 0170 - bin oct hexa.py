

L=[0b11101, 345, 0o2341, 0xfff, 56.8, 1001 ]

for w in L :
    print(f" w= {w:7}, type={type(w)}")


for w in L :
    if type(w) == type(1) :
        print(f" bin(w)= {bin(w)}, type={type(w)}")