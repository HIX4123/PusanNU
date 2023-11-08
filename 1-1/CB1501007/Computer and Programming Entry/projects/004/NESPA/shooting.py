import sys

# 빠른 입출력 함수
input = sys.stdin.readline().rstrip

temp = 0  # 연속 hit에 대해 추가하게 되는 점수
score = 0  # 최종 점수

# 입력받은 텍스트에 대해 반복 구문 수행
for i in input():
    if i == "h":  # 히트한 경우
        temp += 1
        score += temp
    else:  # 아웃한 경우
        temp = 0
        score -= 1

print(score)  # 결과 출력
