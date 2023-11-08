
# 특정 원소가 포함된 index만 뽑아낼 때

la = [ 3, 4, 7, 7, 8, 9, 1, 7, 10, 6, 11, 7]
target = 7

st =  [ i for (i,x) in enumerate( la ) if x == target ]
print(f"target {target}의 위치 index list= {st}")