# 다항식 * 다항식 함수
def multiply_bipolynomial(polynomial1, polynomial2):
    # 초기화
    result = [0] * (len(polynomial1) + len(polynomial2) - 1)
    # 다항식1의 각 항에 대한 루프
    for i, coeff1 in enumerate(polynomial1):
        # 다항식2의 각 항에 대한 루프
        for j, coeff2 in enumerate(polynomial2):
            # 지수법칙 응용
            result[i + j] += coeff1 * coeff2
    return result


# 3개 이상의 다항식 처리 함수
def multiply_polynomials(polynomials):
    # 다항식1 * 다항식2 -> 다항식 리스트
    polynomials[0] = multiply_bipolynomial(polynomials[0], polynomials[1])
    # 이미 사용한 식은 제거
    polynomials.pop(1)
    # 하나만 남을 때까지 재귀함수 적용
    return (
        polynomials[0] if len(polynomials) == 1 else multiply_polynomials(polynomials)
    )


# main
# 최대 10개의 다항식 입력
polynomials = []
for _ in range(10):
    try:
        polynomials.append(list(map(int, input().split()))[::-1])
    except EOFError:
        break

# 출력
print(*multiply_polynomials(polynomials)[::-1])
