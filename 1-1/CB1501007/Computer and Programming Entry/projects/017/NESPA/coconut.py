price = 0
stack = 1
is_consecutive = False # 처음 닫힌 괄호인지 여부

for bracket in list(input()):
    # case '('
    if bracket == "(":
        stack += 1 # 스택 업
        is_consecutive = False
    # case ')'
    else:
        stack -= 1 # 스택 다운
        if stack < 1: # ')'가 더 많이 나온 경우
            price = 0
            break
        # 가장 안쪽 괄호까지 온 경우
        price += 2**stack if not is_consecutive else 0
        is_consecutive = True

# 괄호 쌍 대응 여부 확인
print(price if stack == 1 else 0)
