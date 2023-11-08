
# https://docs.python.org/2/library/array.html


import array

ma = array.array('i', [12,34,56,78,99, 100 ])
print(ma[2], len(ma))

ua = array.array('u', [ "무", "궁", "화", "선", "풍", "기" ])
print(ua[2], len(ua))


da = array.array('d', [ 23.45, 67, 1205.09, 80.123, 100, 0.00034 ])
print(da[2], "len=", len(da), "sum=", sum(da))

print(da)

ma.append(999)
print("\n 뒤에 추가하기", ma)

ma.insert(0,-1000)
print("\n 특정 위치에 삽입", ma)

oa = array.array('i', [7,8,9,10])
ma.extend( oa )
print("\n 확장 후", ma)

ml = [300, 301, 302, 303]

ma.fromlist(ml)
print("\n 리스트의 원소와 합치기", ma)

ma.remove(99)
print("\n 배열에서 특정 원소 99  삭제하기", ma)
# 주의할 것. 없는 원소를 지우면 오류가 발생한다.


