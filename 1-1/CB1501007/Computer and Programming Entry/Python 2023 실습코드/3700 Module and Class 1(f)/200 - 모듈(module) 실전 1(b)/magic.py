

course = "문제해결기법 "
student= "홍길동"
age = 22

def main():
    print("이 문장은 main()에서 출력이 된 것 입니다.")
    print(course, student, age)
    print("모든 출력이 끝났습니다")
    return

def magiccall():
    print( "name of called module ", __name__ )
    print("이 프로그램 다른 어떤 프로그램에서 import된 것입니다. ")

if __name__ == '__main__':
    main()
else :
    print( "name of called module ", __name__ )
    print("이 프로그램 다른 어떤 프로그램에서 import된 것입니다. ")