
# Purpose:  Recursive를 이용해서 powerset(모든 부분집합)  구하기

def powerset(M):
    #L = list(M)
    La=[]
    if len(L)== 0 : return( [ [ ] ] ) # empty set의 power set, base 조건
    else :
        top = L[0]
        L.pop(0)
#       print "In", top, L
        La = powerset(L)
        Q = []
        for x in La :
            #print "x=", x
            tx = list(x)
            tx.append(top)
            Q.append(tx)


        La = La + Q
        return( La )

L = [1,2,3,4,5]
print("List=", L)
Z = powerset( L )
Z.sort()
print("PowerSet(L)=" )
for (i,w) in enumerate(Z) :
    print(f'i={i+1:3}, {w}')


print("Size of PowerSet(L)=", len(Z))


