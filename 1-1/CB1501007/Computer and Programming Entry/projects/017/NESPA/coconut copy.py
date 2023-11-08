price = 0
stack = 1
is_consecutive = False

# 입력받은 문자열을 리스트로 변환하여 하나씩 꺼내서 반복
for bracket in list(input()):
    # 여는 괄호일 경우
    if bracket == "(":
        stack += 1  # 스택에 1 추가
        is_consecutive = False  # 연속적인 괄호 여부 초기화
    # 닫는 괄호일 경우
    else:
        stack -= 1  # 스택에서 1 빼기
        # 스택이 음수가 되면 올바른 괄호 문자열이 아니므로 가격을 0으로 초기화하고 반복문 종료
        if stack < 0:
            price = 0
            break
        # 연속적인 괄호가 아닐 경우 2의 스택 수만큼 가격 추가
        price += 2**stack if not is_consecutive else 0
        is_consecutive = True  # 연속적인 괄호 여부 갱신

# 스택이 0이면 올바른 괄호 문자열이므로 가격 출력, 그렇지 않으면 0 출력
print(price if stack == 0 else 0)
