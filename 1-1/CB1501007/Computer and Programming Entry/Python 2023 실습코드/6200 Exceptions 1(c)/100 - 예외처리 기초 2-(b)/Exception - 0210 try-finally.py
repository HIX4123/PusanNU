
denominator = eval(input( '분모의 값을 입력하시오. '))
try:
    formula = 15/denominator
    print('나눔 결과 =  ' + str(formula))

finally:  # 이 문장은 항상 실행이 됩니다.
    print('으.... 분모가 0이 되면 안됩니다. ')
