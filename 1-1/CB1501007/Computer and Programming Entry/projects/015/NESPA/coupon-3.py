def coupon(sorted_dict):
    def coupon_list(couponlist, total, start, select):
        if select == 0:
            if total <= C and n == len(couponlist):
                coupon_difference = {
                    k: v for k, v in product_list.items() if k not in couponlist
                }
                if min(coupon_difference.values()) > C - total:
                    coupon_list2.append(couponlist)
                    return
        if total > C or start == n:
            return
        coupon_list(
            couponlist + [sorted_dict[start][0]],
            total + sorted_dict[start][1],
            start + 1,
            0,
        )
        coupon_list(couponlist, total, start + 1, 1)

    coupon_list2 = []
    coupon_list([], 0, 0, 0)
    coupon_list2 = sorted([sorted(result) for result in set(map(tuple, coupon_list2))])
    for result in coupon_list2:
        print(*result)


product_list = {}
n, C = map(int, input().split())
product_list = {i + 1: int(input()) for i in range(n)}
sorted_dict = sorted(product_list.items(), key=lambda item: item[1])
coupon(sorted_dict)
