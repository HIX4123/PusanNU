
import traceback

print(" 디버깅을 어떻게 하는지 살펴 봅니다")

def createException(name):
    print(">>> ", name, " <<<<")
    raise Exception( '발생한 오류의 종류 = ' + name )

createException( 'Summer')


