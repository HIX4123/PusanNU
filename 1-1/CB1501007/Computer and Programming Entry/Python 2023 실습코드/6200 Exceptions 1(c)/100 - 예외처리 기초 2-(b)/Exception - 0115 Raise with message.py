
a = int(input("1~5 까지 숫자 입력 : ")) # 범위를 벗어나면 error 발생!

if a < 1 or a > 5:
    raise Exception("정신을 차리라고,,,이 사람아. 에러야 에러!!") # 범위 안에 있으면 정상 출력

print(f"입력한 a : {a} 입니다.")

