
# Purpose:  Recursive를 이용해서 powerset(모든 부분집합)  구하기

def maxorder( L, C ):
    #L = list(M)
    La=[]
    if len(L) == 0 : return( [[ ]] ) # empty set의 power set, base 조건
    if len(L) == 1 :
        if L[0] < C : return ( [ [L[0]] ] )
        else : return ( [[ ]] )

    # 그외 경우, 원소가 2개 이상인 경우
    # L[0]를 사용하지 않는 경우
    top = L[0]
    L.pop(0)
    La = maxorder(L, C )

    # L[0]를 사용하는 경우
    if top < C :
        Lb = maxorder( L, C-top )
    else :
        Lb = maxorder( L, C )

    print("Lb = ", Lb, "C=", C )

    for w in Lb :
        w.append( top )

    Lab = La + Lb
    return( Lab )

L = [4500, 1200, 800, 2100, 1700]

print("List=", L)
Z = maxorder( L, 5000 )
print(" maxorder(L)=", Z)



