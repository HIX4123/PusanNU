
# import에도 두 가지 방법이 있습니다.
# 방법 1) import 모듈 X
# 방법 2) from 모듈 import 변수나 함수

# 첫번째 방법1)은 모듈 전체를 가져옵니다. 사용할 때에는 X.name으로 부릅니다.
# 두번째 방법2)는 모듈 내에서 필요한 것만 가져오는 방법입니다.
# 그러나 방법2)는 name space로 Qualifying을 하지 않기 때문에
# 박치기를 할 수 있어 사용할 때에 이런 상황을 조심해야 합니다.
# 같은 이름의 경우 마지막 선언된 것으로 update 됩니다.


from Box import foo, stars
from Bus import foo


print("첫번째 Call = ", foo)
print("두번째 Call = ", foo)

print("We Call stars() = ")
stars()

