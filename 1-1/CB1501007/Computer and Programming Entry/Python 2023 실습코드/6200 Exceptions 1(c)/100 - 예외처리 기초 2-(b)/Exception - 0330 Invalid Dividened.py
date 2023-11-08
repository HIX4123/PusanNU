
try:
    a = int(eval(input( '피제수를 입력하세요: ')))
    b = int(eval(input( '제수를 입력하세요: ')))
    if a <= 0 or b <= 0:
        raise ArithmeticError( '피제수 혹은 제수가 0 이하일 수 없습니다.')
    else :
        print(a, "/", b, ' =', a/b)

except ArithmeticError as e:
    print('예외 발생:', e.args[0])

