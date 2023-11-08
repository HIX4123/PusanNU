
# 다음은 8명의 6과목 성적이 기록된 list를 나타내고 있다.
# 각 리스트 원소의 첫 원소는 해당자의 이름이다. 그리고 이어
# 다음 6개의 숫자는 각 6과목의 성적을 나타낸다.

def printname( XL ) :
    n = len(XL)
    print("\n 성적표의 이름을 한 줄에 모두 출력합니다.")
    for i in range(n) :
        print(" ", XL[i][0], end=' ')
        if (i+1) % 4 == 0 : print("\n ")

# ---------- end of function printname() -------------

dlist = [   ["Amos",   45,  3, 86, 45, 67, 54], \
            ["Berry",  23, 73,  6, 15, 67, 84], \
            ["Colins", 54, 40, 70, 87, 12, 10], \
            ["David",   5, 87, 45, 15, 45, 81], \
            ["Zerony",  7, 60, 90, 43, 33, 16], \
            ["Mariam", 94, 13, 44,  5,  7,  0], \
            ["Soltan", 15, 19, 50, 22, 27, 77], \
            ["Quany",  50, 20, 60, 15, 34, 80], \
            ["Periln",  1,  7, 35, 45, 43, 53],  ]


print(dlist)

printname( dlist )