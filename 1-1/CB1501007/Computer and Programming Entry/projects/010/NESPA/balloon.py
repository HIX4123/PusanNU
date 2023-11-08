from sys import stdin
import numpy

input_func = stdin.readline


# 한쪽 끝 점과 원의 중심으로 이루어지는 삼각형의, 원의 중심쪽 각을 구하는 함수
def get_radian(width, height):
    return numpy.arctan(width / height)


# 원 양쪽의 두 각도를 *2해 2pi에서 뺀 중심각을 계산하고 이를 통해 호의 길이를 계산하는 함수
def get_arc(angle1, angle2):
    return (2 * numpy.pi - 2 * (angle1 + angle2)) * r


# main
for _ in range(3):
    # 입력
    x, r, n = map(int, input_func().split())
    # 양쪽의 각도 계산
    angle1, angle2 = get_radian(x, r), get_radian(n - x, r)
    # 호의 길이와 나머지 직선부분(=n과 길이가 같음)을 더해서 최종 길이 구하기. 그리고 올림
    print(int(numpy.ceil(get_arc(angle1, angle2) + n)))
