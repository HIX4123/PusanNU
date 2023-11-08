import importlib  # importlib.reload(mymoda)

#reload(magic) # 새로 compile된 경우 이전의 pyc를 버리기 위해서 새로 load해야 한다.
               # 그렇지 않으면 magic.py를 고쳐도 반영되지 않는다.

import magic  # import는 pyc가 있으면 그것을 먼저, 없으면 py를 pyc로 만들어 입력

print("1>>", magic.course)
print("2>>", magic.student)
print("3>>", magic.age)

def main():
    print("이 문장은 all-magic.py 출력이 된 것 입니다.")
    return

if __name__ == '__main__':
    main()
else :
    print("이 프로그램 call-magic.py는 main이 아닙니다.")


magic.magiccall()