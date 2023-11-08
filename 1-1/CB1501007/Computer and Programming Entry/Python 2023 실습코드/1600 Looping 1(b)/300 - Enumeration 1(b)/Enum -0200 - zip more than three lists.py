
la = list(zip([1, 2, 3], "abc", [True, False, None]))
print(la)

lp = [1,2,3,4,5]
lq = [6,7,8,9,10]
lw = [-1,1,-1,1,3]


for a,b,c in zip( lp, lq, lw) :
    print((a,b,c))


lz = list(zip ( lq, lp, lw))
print(lz)


names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(list(zip(names,grades)))
print(d)
