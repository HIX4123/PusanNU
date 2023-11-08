
print(" 디버깅을 어떻게 하는지 살펴 봅니다")

try:
    x = eval(input( ' 1-10 사이의 값을 입력하시오. : '))
    if x<1 or x>10:
        raise Exception
    print(' Great! 올바른 값을 입력했습니다. ')

except:
    print(' Oops! 잘못된 값을 입력해서 except가 발생했습니다. ')
