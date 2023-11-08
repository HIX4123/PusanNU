#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-05-13
#-------------------------------------------------------------------------------

name="조환규0"
dept="부산대학교"
wish="롯데야 야구 쫌 잘해라!"

def main():
    print("여기는 XYZ.py")
    CL=[name, dept, wish]
    for w in CL :
        print(f"w= {w}")

if __name__ == '__main__': #자체로 수행
    main()
else :
    print("이 XYZ.py는 import가 되었습니데이")


#요놈이 import가 되면 __name__ != '__main__':


