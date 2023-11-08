
import copy

def Lput(L, d):
    for w in L :
        w.append(d)


def pows( L ):
    if len(L) <= 0 :
        NL = [[]]
        return( NL )
    else : # 1개 이상의 원소가 있음.
        Lx = copy.deepcopy(L)
        d = Lx.pop(0)   # 첫번째 원소 삭제
        La = pows( Lx )  # 첫번째 원소가 삭제된 집합의 powerset
        Lb = copy.deepcopy( La ) # 그것을 Lb로 복사
        for w in Lb :
            w.append(d)          # Lb의 모든 원소에 d를 추가함.

        La.extend( Lb )      # 두 집합을 합침.
        return( La )


la =[1,2,3,4,5,6]

pl = pows( la)
print("Power Set 출력", end=' ')
for w in pl :
    print(w)
print("size=", len(pl))