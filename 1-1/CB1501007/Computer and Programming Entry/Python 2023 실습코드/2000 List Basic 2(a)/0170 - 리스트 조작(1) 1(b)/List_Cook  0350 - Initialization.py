

nl = [ None]        #Null List
ml = [1,2,3,4,5]

print("\n 실험 1")
print(nl, ml)


nnl = nl * 5
mml = ml * 5

print("\n 실험 2")
print(nnl)
print(mml)

verta = [ "x" for x in range(12)]
vertb = [[ 2016 for x in range(5)] for y in range(10)]

print("\n 실험 3")
print(verta)
print(vertb)

x1=11
x2=16
list2 = [x*0.5 for x in range(2*x1, 2*x2+1)]
print("\n 실험 4")
print(list2)

