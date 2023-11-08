
# Purpose: 이중 리스트 구조 (리스트의 원소가 또 하나의 리스트가
#
#   3   7  12   5
#   7   0   5  -3
#  -9   3   4  12
#   6   8  -5   4
#

print(" 4 X 5 행렬에서의 계산")
mtx=[ [ 3, 7, 12,  5],
      [ 7, 0,  5, -3],
      [-9, 3,  4, 12],
      [ 6, 8, -5,  4],
      [ 0, 1,  3,  3],  ]


for this in mtx :
    print("각 줄(row)별 ", this)

print("이중 리스트의 모든 원소 출력하기")
for row in range( len(mtx )) :
    for col in range( len( mtx[0] )) :
        print("(",row+1,",",col+1,")=", mtx[row][col])

# 대각선 원소를 출력해보기. 양쪽 모두

