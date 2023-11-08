#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

def my_function():
    """  이 함수는 블라블라 하는 함수로서s
       and does nothing really."""
    return None

def your_function():
    """ 이렇게 표시하면 나중에
    help를 쉽게 만들 수 있다."""
    return None

print ( "Using __doc__:" )
print ( my_function.__doc__ ) # 특정 함수의 설명문을 출력할 수 있다.
                              # 나중에 사용자 manual 만들 때 사용된다.

print( "Using help:" )
print (help( your_function) )
