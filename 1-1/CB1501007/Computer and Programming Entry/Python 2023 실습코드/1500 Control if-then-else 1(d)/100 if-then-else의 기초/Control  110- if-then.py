# 프로그램 구성의 기초에 대하여 배웁니다.
#  이번 실습에서 이해해야 할 사항
#  부모 문장과 자식문장, 자식문장은 부모문 다음에 들어가되
#  반드시 한 Tab key를 넣은 뒤에 들어가야 한다.

# Indentation (들여쓰기)
# 부모 문장, 자식문장, 손자 문장


a = 1000
b = 500
if ( a == 1000 ) and (b== 500) :
    print("두 개가 일치를 합니다.")
else :
    print("일치하지 않습니다")

if ( a == 1000 ) or (b== 501) :
    print("두 개가 일치를 합니다.")
else :
    print("일치하지 않습니다")

if 23 > 67 : print("참")  # : 다음에 붙혀도 상관없다
else : print("거짓")      # 이것이 더 깔끔하게 보일 수 있다.


