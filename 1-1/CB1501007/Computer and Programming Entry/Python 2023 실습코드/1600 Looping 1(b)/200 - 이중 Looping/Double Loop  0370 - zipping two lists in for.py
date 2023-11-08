

ka = [ "good",     "crazy", "happy", "sad", "kong" ]
kb = [ "gorilla",  "cat",   "hama",  "salmon" ]


for x,y in zip(ka, kb) :
    t = x + "-" +  y
    print(t)


la = [  1, 2,  3, 4,  5,   6]
lb = [ 34, 5, -9, 0, 55, 100, 600, 8]  # 개수가 다를 경우에는 짧은 쪽으로

lc = [ x +y for x,y in zip(la,lb)]
print(lc)