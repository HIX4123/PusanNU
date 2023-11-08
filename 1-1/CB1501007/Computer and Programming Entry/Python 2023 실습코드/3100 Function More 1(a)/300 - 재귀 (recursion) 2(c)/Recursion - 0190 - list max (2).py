
# Purpose: 재귀식을 이용해서 for loop없이 최대값을 구하기



def recur_max(L) :
    if len(L) == 1 : return L[0] # 원소가 1개이면 그것이 최대값!!!! 기저(base)조건

    mid = len(L)/2
    a= recur_max( L[0: mid] )  # 리스트의 앞부분 반에서의 최대값
    b= recur_max( L[mid: ]  )  # 리스트의 뒷부분 반에서의 최대값
    return max(a,b)

myl = [ 25, 3, 5, 65, 21, 67, 11, 34 ]

print("주어진 리스트", myl)
print("list의 최대값", recur_max( myl ))