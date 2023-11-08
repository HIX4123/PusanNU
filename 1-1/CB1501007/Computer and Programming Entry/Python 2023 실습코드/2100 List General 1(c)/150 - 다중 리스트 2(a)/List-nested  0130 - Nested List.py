

Dlist = [ [ 1,  2,  3,  4,  5],
          [ 6,  7,  8,  9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25],
        ]

print(f"\n Column 성분 출력하기 ")
for c in range(5):
    for r in range(5):
        print(f" {Dlist[r][c]}", end="")
    print("\n")

print(f"\n 대각성분 출력하기 ")
for w in range(5):
    print(f" Dlist[{w}][{w}]= {Dlist[w][w]}")