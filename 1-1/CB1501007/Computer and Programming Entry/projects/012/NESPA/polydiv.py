def monodivide(dividend, divisor, stack=0):
    # 피제수의 최고차항 // 제수의 최고차항 = 몫
    quotient = dividend[stack] // divisor[0]
    # 몫 반환
    yield quotient
    # 뺄셈 연산
    for i, d in enumerate(divisor):
        dividend[stack + i] -= d * quotient
    # 나눗셈 완료 판단, 재귀함수 처리
    if stack + len(divisor) != len(dividend):
        yield from monodivide(dividend, divisor, stack + 1)
    # 나눗셈 완료 시
    else:
        yield dividend


def print_answer(divided):
    # 몫, 나머지 분리
    quotients, remainder = divided[:-1], divided[-1]
    # 0 제거 작업
    while remainder[0] == 0 and len(remainder) > 1:
        remainder.pop(0)
    # 출력
    print(*quotients)
    print(*remainder)


# main
# 두입력값을 리스트로 변환해 monodivide -> print_answer 순서로 처리
print_answer(
    list(monodivide(list(map(int, input().split())), list(map(int, input().split()))))
)
