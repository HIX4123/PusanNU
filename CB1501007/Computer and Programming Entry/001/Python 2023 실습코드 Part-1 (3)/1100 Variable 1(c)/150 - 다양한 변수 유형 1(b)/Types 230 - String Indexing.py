#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

query = "good"   # 문자열 찾기의 유연성
text =  "This is a good beer"
if query in text :
    print("Yes, it is in")

print((text[0:5]))     # 앞에서 4 문자
print((text[-7:]))     # 뒤에서 7문자 string


msg = "동수야... 오늘 보드 게임장.. ㅋㅋ ㅋ 오라"

bword = "ㅋㅋㅋ"

if bword in msg :
    print("착한 말을 사용합시다")
else :
    print(" msg는 착한 말만 있습니다. ")
