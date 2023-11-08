def monodivide(dividend, divisor, stack=0):
    # 첫번째 인덱스의 값을 나누는 수로 나눈 몫을 구한다.
    quotient = dividend[stack] // divisor[0]
    # 몫을 반환한다.
    yield quotient
    # 나누는 수로 나눈 값을 나누는 수로 곱한 값을 나누는 수로 뺀다.
    for i, d in enumerate(divisor):
        dividend[stack + i] -= d * quotient
    # 나누는 수로 나눈 값이 나누는 수의 길이와 같지 않으면 재귀호출한다.
    if stack + len(divisor) != len(dividend):
        yield from monodivide(dividend, divisor, stack + 1)
    # 나누는 수로 나눈 값이 나누는 수의 길이와 같으면 나머지를 반환한다.
    else:
        yield dividend


def print_answer(divided):
    # 몫과 나머지를 구한다.
    quotients, remainder = divided[:-1], divided[-1]
    # 나머지의 첫번째 값이 0이면 제거한다.
    while remainder[0] == 0 and len(remainder) > 1:
        remainder.pop(0)
    # 몫과 나머지를 출력한다.
    print(*quotients)
    print(*remainder)


# 입력받은 값을 리스트로 변환하여 monodivide 함수에 전달하고, 그 결과를 print_answer 함수에 전달하여 출력한다.
print_answer(
    list(monodivide(list(map(int, input().split())), list(map(int, input().split()))))
)
