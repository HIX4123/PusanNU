dan=list("일이삼사오육칠팔구")

for f in range(2,10):  # 2,...8,9
    print("\n", dan[f-1],"단 입니다.")
    for s in range(1,10):
        print(f'{f} x {s}= {f*s:3}')

