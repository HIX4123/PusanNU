
def raiseErrorFunction():
    num = input( "숫자를 입력하세요 : ")

    if not num.isdigit():  #숫자여부판단
        #예외발생
        raise Exception("유효하지 않은 숫자입니다.({0})".format(num))
    else:
        print(("입력한 수는 {0} 입니다.".format(num)))

try:
    raiseErrorFunction()
except Exception as err:
    print(("예외발생 : {0}".format(err)))

