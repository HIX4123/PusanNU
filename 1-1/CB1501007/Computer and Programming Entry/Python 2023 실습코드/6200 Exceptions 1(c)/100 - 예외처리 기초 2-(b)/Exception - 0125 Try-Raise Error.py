
# TRY-EXCEPT는 NORMAL    exit로 메시지를 생산한다.

try:
    a = int(input("1~5 까지 숫자 입력 : ")) # 범위를 벗어나면 error 발생!
    if a < 1 or a > 5: raise # 범위 안에 있으면 정상 출력
    print(f"입력한 a : {a} 입니다.")

except:
    print("분명히 1~5 사이 숫자를 입력하라고 했는데.. 디질래 ?")

