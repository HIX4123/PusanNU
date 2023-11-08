# 가져온 모듈 해제하기, 다시 가져오기
# import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있습니다.


import math

print(math.sqrt(1234))

del math  # 올려진 module을 삭제. 왜 ? 시스템이 너무 무거워지면

#print(math.sqrt(1234)) # Error 나용

# 모듈을 다시 가져오려면 importlib.reload를 사용합니다.
import importlib
import math

importlib.reload(math)  # 개인용 모듈인 경우 recompile된 것을 올림

print(math.sqrt(3456))



