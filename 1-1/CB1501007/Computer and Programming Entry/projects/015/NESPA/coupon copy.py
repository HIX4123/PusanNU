from cProfile import run

def main():
    from sys import stdin

    # 표준 입력으로부터 문자열을 읽어들이는 함수를 input_str 변수에 할당
    input_str = stdin.readline

    # 물건의 개수와 예산을 입력받음
    num_items, budget = map(int, input_str().split())

    # 물건의 가격을 입력받아 리스트에 저장
    prices = [int(input_str()) for _ in range(num_items)]

    # 메모이제이션을 위한 딕셔너리
    memo = {}

    # 선택된 물건과 선택되지 않은 물건의 가격을 계산하는 함수
    def compute_price(selected, unselected):
        # 선택된 물건과 선택되지 않은 물건의 가격을 튜플로 묶어서 key로 사용
        key = (tuple(selected), tuple(unselected))
        # 메모이제이션된 결과가 있으면 반환
        if key in memo:
            return memo[key]
        # 선택된 물건의 가격의 합
        total_price = sum(selected)
        # 선택되지 않은 물건 중 가격이 가장 작은 것
        min_price = min(unselected, default=1)
        # 선택된 물건의 가격의 합과 선택되지 않은 물건 중 가격이 가장 작은 것을 튜플로 묶어서 결과로 반환
        result = (total_price, min_price)
        # 메모이제이션에 결과 저장
        memo[key] = result
        return result

    # 모든 물건의 조합을 검사
    for active in range(2**num_items - 1, -1, -1):
        # 현재 검사 중인 물건의 조합을 이진수로 변환하여 리스트로 저장
        active_bits = list(map(int, f"{active:b}".zfill(num_items)))
        # 선택된 물건과 선택되지 않은 물건을 구분하여 리스트에 저장
        chosen, unchosen = [], []
        for price, bit in zip(prices, active_bits):
            (chosen if bit else unchosen).append(price)
        # 선택된 물건과 선택되지 않은 물건의 가격을 계산
        total_price, min_price = compute_price(chosen, unchosen)
        # 예산 범위 내에서 가격의 합이 최대인 물건의 조합을 출력
        lower_limit = budget - min_price
        if budget >= total_price > lower_limit:
            print(*(i + 1 for i, bit in enumerate(active_bits) if bit))



if __name__ == '__main__':
    run("main()")