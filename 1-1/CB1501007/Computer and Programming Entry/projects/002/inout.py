# 3월 13일 실습용 코드입니다.


i = 0
while( True ):
    i = i + 1
    myin = input("> 문자열을 입력하시오: ")
    if myin == "끝" or myin == "end" :
        print("> 전체 프로그램을 종료합니다. 안뇽!! ")
        exit()
    else :
        print(f"{i:2} > 입력 문자열의 길이 : {len(myin)}")