#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
"""
파이썬에서 언더스코어(_)는 다음과 같은 상황에서 사용되는데 크게 5가지의 경우가 있다.
    •인터프리터(Interpreter)에서 마지막 값을 저장할 때

    •값을 무시하고 싶을 때 (흔히 “I don’t care”라고 부른다.)

    •변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때

    •국제화(Internationalization, i18n)/지역화(Localization, l10n) 함수로써 사용할 때
    •숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때
"""

# 파이썬 인터프리터에선 마지막으로 실행된 결과값이 _라는 변수에 저장된다. 이는 표준 CPython 인터프리터에서 먼저 사용되었으며 다른 파이썬 인터프리터 구현체에서도 똑같이 사용할 수 있다.
# >>> 10
# 10
# >>> _
# 10
# >>> _ * 3
# 30
# >>> _ * 20
# 600



class MyClass():
    def __init__(self):
        print("OWK")


def my_defination(var1 = 1, class_ = MyClass):
    print ( var1 )
    print ( class_)

print( my_defination() )




