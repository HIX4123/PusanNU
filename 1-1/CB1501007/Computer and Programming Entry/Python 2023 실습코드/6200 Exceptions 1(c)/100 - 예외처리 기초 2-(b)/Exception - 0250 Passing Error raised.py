
try:
    f = open( "xsample.txt", 'r')
#except IOError :      #python 2.7에서 사용하는 방법
except FileNotFoundError:  #python 3.x에서 사용하는 방법
    print("우리는 Error를 그냥 무시합니다.")
    pass
