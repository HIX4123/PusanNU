
Tlist= [  ("mood",0,1), \
          ("mood",5,0), \
          ("good",2,1), \
          ("food",3,2), \
          ("food",2,1), \
          ("food",2,3), \
          ("good",3,0), \
          ("food",3,3), \
          ("good",3,3), \
          ("food",0,1), \
          ("mood",3,2), \
       ]

def myfunc(w):
    return (w[1], w[0], w[2])

X =sorted(Tlist)
for w in X :
    print(w)

print("\n\n 다른 기준으로 tuple sort")
X =sorted(Tlist, key=myfunc)
for w in X :
    print(w)