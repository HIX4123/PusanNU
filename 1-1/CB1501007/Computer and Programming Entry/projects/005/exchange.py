import sys

input = sys.stdin.readline  # 빠른 입출력 함수

e = int(input())  # Euro, 환율 입력
k = int(input())  # KRW, 준비한 액수 입력

# 유로화 교환
exchange = k // e  # 환전액수, 나머지 버림.

# 수수료 공제
if exchange < 100:
    exchange -= 1

# 지폐 분배
h, exchange = exchange // 100, exchange % 100  # Hundred, 100유로 단위 환전, 나머지를 exchange에 저장
f, exchange = exchange // 50, exchange % 50  # Fifty, 50유로 단위 환전, 나머지를 exchange에 저장
t, u = exchange // 10, exchange % 10  # Ten, 10유로 단위 환전, 나머지를 Unit, 1유로 단위 환전

print(h, f, t, u)
