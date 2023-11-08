
# Purpose:  recursion을 이용해서 모든 쌍을 리스트로 출력하기

def allpair( L ): #리스트의 모든 쌍을 list에 담아서 출력한다.
    if len(L) <= 1 : return ([])
    if len(L) == 2 : return( [ [L[0],L[1] ] ] )

    first = L[0]
    caseA= [ ]
    for x in L[1:] :
        caseA.append( [ first, x ])

    L.pop(0) # 첫번째 원소를 제거한 리스트
    caseB = allpair( L ) #그것의 모든 pair를 계산

    caseB.extend( caseA ) #1번을 포함한 pair 원소를 합침.
    return( caseB )
# -------- end of allpair --------------




xlist = [1,2,3,4,5,6,11]
result= allpair( xlist )
result.sort()  #보기좋게 출력함
print(result)



