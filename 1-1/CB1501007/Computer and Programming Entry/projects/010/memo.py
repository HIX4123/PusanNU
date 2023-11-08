# from operator import itemgetter

# food = [["국밥", 7500], ["커피", 3200], ["공기밥", 1500], ["우유피", 1800], ["피자밥", 9800], ["생수", 900], ["김밥", 2700], ["TOP", 5600]]

# print(sorted(food, key=itemgetter(1), reverse=True))

# ------------------------------------------------------------------

# S = [
#     ("Kim", 34, 45, 27),
#     ("Han1", 64, 56, 34),
#     ("Moon", 29, 78, 23),
#     ("Han2", 67, 98, 27),
#     ("Mook", 45, 78, 52),
#     ("Cho", 16, 9, 12),
# ]


# def ssum(t):
#     return t[1] + t[2] + t[3]

# S.sort(key=ssum, reverse=True)

# for w in S:
#     print(">", w[0], "sum =", ssum(w))

# ------------------------------------------------

P = [(52, 14), (45, 5), (45, 4)]


def mymy(t):
    return t[0], -t[1]


P.sort(key=mymy)
print(P)
