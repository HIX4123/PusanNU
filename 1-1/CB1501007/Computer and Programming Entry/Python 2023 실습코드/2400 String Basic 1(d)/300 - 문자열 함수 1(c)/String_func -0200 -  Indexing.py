

# 문자열 인덱싱(indexing)

# 아주 중요한 개념. 리스트와 문자열의 차이.
# 리스트는 사용자가 뭔가 변환시킬 수 있는 mutable 구조이지만
# 문자열은 immutable object이다.


myl =[34,56,78,90, 11]
print("myl=", myl)
print("myl[1]=", myl[1])
myl[1]=-89
print("myl=", myl)

mystr="Computers"
print(mystr[1])
# mystr[1]="q"  # 이것은 안됨. String은 컴퓨터가 보호하고 있다. 변경불가!!

import string

xx = "한글문자와 유니코드"
print(xx, len(xx), len(str(xx)))
print('Ham \uB610 Beer')



x = 'I Love Programming So MUCH'
print(x)
for w in x:
    if( w in string.ascii_uppercase):
        print("대문자", k)