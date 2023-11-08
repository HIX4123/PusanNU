import sys

#입력
I = sorted(list(map(int, sys.stdin.readline().split()))) # a의 값을 받아 리스트에 정렬

#예외 처리: case '0' 우선 판별
if I[2] >= I[0] + I[1]: #가장 긴 변이 나머지 두 변의 합보다 큰 경우
    print('0')          #0을 출력하고
    exit()              #exit

#피타고라스 공식의 양변을 변수화
ao = I[0]**2 + I[1]**2  # A(djacent)O(pposite) : 밑변과 높이의 제곱의 합
h = I[2]**2 # H(ypotenuse) : 빗변의 제곱

#main
if ao == h: #case: 직각삼각형
    print('1')
elif ao < h:#case: 둔각삼각형
    print('2')
else:       #case: 예각삼각형
    print('3')