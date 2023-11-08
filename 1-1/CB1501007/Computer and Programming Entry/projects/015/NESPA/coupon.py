# input
num_menus, coupon_value = map(int, input().split())
menu_prices = [int(input()) for _ in range(num_menus)]

# initiation
visited = [False] * num_menus
cache = []


# 깊이 우선 탐색 알고리즘
def DFS(coupon, start=0):
    # 쿠폰으로 구매할 수 있는 최소 가격 초기화
    min_price = coupon_value
    for i in range(num_menus):
        # 이미 확인한 메뉴나 쿠폰으로 구매할 수 없는 메뉴인 경우
        if visited[i] or menu_prices[i] > coupon:
            continue
        # 최저가 갱신
        min_price = menu_prices[i]
        # 이전에 선택한 메뉴보다 앞에 있는 메뉴인 경우
        if i < start:
            continue
        # 메뉴 확인 표시
        visited[i] = True
        # 캐시 갱신
        cache.append(i + 1)
        # 다음 메뉴 확인
        yield from DFS(coupon - menu_prices[i], i + 1)
        # 메뉴 확인 취소
        visited[i] = False
        # 트리 후진
        cache.pop()

    # 더 이상 구매할 수 없는 경우
    if min_price > coupon:
        yield cache[:]


# output
for i in DFS(coupon_value):
    print(*i)
