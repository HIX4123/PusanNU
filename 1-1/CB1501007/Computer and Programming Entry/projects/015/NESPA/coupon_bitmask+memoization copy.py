from cProfile import run


def main():
    from sys import stdin

    input_str = stdin.readline

    # 물건의 개수와 예산 입력
    num_items, budget = map(int, input_str().split())

    # 물건의 가격 입력
    prices = [int(input_str()) for _ in range(num_items)]

    # 메모이제이션 딕셔너리
    cache = {}

    # 메모이제이션 함수
    def memoization(arg):
        # arg가 0일 경우 0을 반환
        if arg == 0:
            return 0
        # arg가 1일 경우 가장 비싼 물건의 가격을 반환
        elif arg == 1:
            return prices[-1]
        # arg가 cache에 없을 경우
        if arg not in cache:
            # arg의 이진수 표현에서 가장 높은 자리수를 찾음
            if arg >> (arg.bit_length() - 1) == 1:  # case 1
                # 가격을 더해서 저장
                cache[arg] = prices[-arg.bit_length()] + memoization(
                    arg - (1 << (arg.bit_length() - 1))
                )
            else:  # case 0
                # 하위 가격 그대로 저장
                cache[arg] = memoization(arg - (1 << (arg.bit_length() - 1)))
        return cache[arg]

    asdf = []
    # 모든 물건을 포함하는 경우부터 시작하여 1씩 줄여가며 예산 내에서 최대 가격을 만드는 경우 탐색
    for active in range(2**num_items):
        # 현재 상태에서의 총 가격 계산
        total_price = memoization(active)
        # 현재 상태에서의 하한 가격을 찾기 위해 현재 상태에서 포함되지 않은 물건들의 가격 중 가장 작은 값을 찾음
        lower_limit = budget - min(
            [
                value
                for index, value in enumerate(prices)
                if active != active | 1 << num_items - (index + 1)
            ],
            default=budget,
        )
        # 예산 내에서 최대 가격을 만드는 경우를 찾았을 경우 해당하는 물건들의 인덱스를 출력
        if budget >= total_price > lower_limit:
            asdf.append(
                [
                    i
                    for i in range(1, num_items + 1)
                    if active == active | 1 << num_items - i
                ]
            )

    for i in reversed(asdf):
        print(*i)


if __name__ == "__main__":
    run("main()", sort="tottime")
