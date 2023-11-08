# |이 코드는 예산 내에서 최대 가격을 만드는 경우를 찾는 문제를 해결하는 코드입니다.
# |
# |좋은 점:
# |- 메모이제이션을 사용하여 중복 계산을 피하고 실행 시간을 단축시킵니다.
# |- 이진수 표현을 사용하여 현재 상태에서 포함되지 않은 물건들의 가격 중 가장 작은 값을 찾는 등, 효율적인 알고리즘을 사용합니다.
# |
# |나쁜 점:
# |- 변수명이 모호합니다. 예를 들어, `active` 변수는 현재 상태를 나타내는데, 이름만 보고는 이해하기 어렵습니다.
# |- 코드의 가독성이 떨어집니다. 특히, 이진수 표현을 사용하는 부분은 이해하기 어렵습니다.
# |- 코드의 구조가 복잡합니다. 이 코드를 처음 보는 사람은 이해하기 어려울 수 있습니다.
# |
# |따라서, 이 코드의 가독성을 높이고 변수명을 명확하게 바꾸는 등의 개선이 필요합니다.
# |
from sys import stdin

input_str = stdin.readline

# 물건의 개수와 예산 입력
num_items, budget = map(int, input_str().split())

# 물건의 가격 입력
prices = [int(input_str()) for _ in range(num_items)]

# 메모이제이션 딕셔너리
cache = {}


# 메모이제이션 함수
def memoization(n):
    # n이 0일 경우 0을 반환
    if n == 0:
        return 0, budget
    # n이 1일 경우 가장 비싼 물건의 가격을 반환
    elif n == 1:
        return prices[-1], budget - prices[-1]
    
    # n이 cache에 없을 경우
    if n not in cache:
        # n의 이진수 표현에서 가장 높은 자리수를 찾음
        if n >> (n.bit_length() - 1) == 1:  # case 1
            # 가격을 더해서 저장
            sum_price, max_limit = memoization(n - (1 << (n.bit_length() - 1)))
            sum_price += prices[-n.bit_length()]
            max_limit -= prices[-n.bit_length()]
        else:  # case 0
            # 하위 가격 그대로 저장
            sum_price, max_limit = memoization(n - (1 << (n.bit_length() - 1)))
        cache[n] = sum_price, max_limit
    return cache[n]


result = []
# 모든 물건을 포함하는 경우부터 시작하여 1씩 줄여가며 예산 내에서 최대 가격을 만드는 경우 탐색
for active in range(1, 2**num_items):
    # 현재 상태에서의 총 가격 계산
    total_price, lower_limit = memoization(active)
    # 현재 상태에서의 하한 가격을 찾기 위해 현재 상태에서 포함되지 않은 물건들의 가격 중 가장 작은 값을 찾음
    # 예산 내에서 최대 가격을 만드는 경우를 찾았을 경우 해당하는 물건들의 인덱스를 출력
    if budget >= total_price > lower_limit:
        result.append(
            [
                i
                for i in range(1, num_items + 1)
                if active == active | 1 << num_items - i
            ]
        )

for i in reversed(result):
    print(*i)

# #시간 측정에 사용 중인 입력값
# 20 50000
# 11111
# 22222
# 33333
# 44444
# 1111
# 2222
# 3333
# 4444
# 5555
# 111
# 222
# 333
# 444
# 555
# 11
# 22
# 33
# 44
# 55
# 25000
