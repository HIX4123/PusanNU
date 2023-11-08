# 작은 따옴표와 근 따옴표는 번걸아가면서 사용할 수 있다.

a = 'baseball'
b = "football"
c = " 'figure skate' "
d = ' Tom said to me, "Who are you ? ". We escaped '
e = " Tom said to me, \"Who are you ? \". We escaped \'"
kor = """ 한 라인을 넘어가는 특별한 스트링을
      만드는 방법은 3개의 더불 쿼터를 사용하는 것이다"""

print(a, b, c)
print("d = ", d)
print("e = ", e)
print("하나 이상의 문자열 =", kor)


mycode = "Oh my God, Please give me A+"
pattern = "Oh"

what = pattern in mycode  # 특정한 문자열이 전체에 있는지 검사
if what :
    print("Oh가 있습니다.")
else :
    print("Oh는 없습니다.")

# print mycode.upper()

# 실습문제
# 스트링 변수를 치고 점(.)을 치면 문자열에 관련된 다양한
# method( )가 나열됩니다. 이 중에서 3개만 골라서 수행해보고
# 그것이 어떤 의미인지 설명하시오.


# 생 문자열 raw string r'~~~'

print("갑니다" , 'C:\\nowhere')
print("또갑니다" , r'C:\\nowhere')  # raw, 날 것으로 그대로 저장, special case 처리중지

tmp01 = "1230232923"
tmp02 = "123banan"
print(tmp01.isnumeric())
print(tmp02.isnumeric())

strw = "this2009";
print(strw.isdecimal());

strw = "23443434";
print(strw.isdecimal());

strw = "---";
seq = ("a", "b", "c"); # This is sequence of strings.
print(strw.join( seq ));