# 좀 더 쉽게 변수를 문자열 포맷을 이용하여 출력하는 법을 배웁니다.
# 문자열의 서식 지정

format = 'name = %s  age = %s'
str1 = 'Book'
str2 = 'Created'
# 포맷의 입력은 반드시 tuple로 공급된다.
print(format % (str1, str2 ))

dongari = '''
----------------------
%s 회원님

안녕하셨습니까 ? 이번에 우리 동아리에서는
봄을 맞이하여 %s로 MT를 떠납니다.
참가 회비는  %d-원  입니다. 많이 참석하여
즐거운 시간을 가지시기 바랍니다.

회장 일수꾼 올림
-------------------------'''
print(dongari % ('강당수', '요단강', 14500))

mem1 = ( 'Tom', 'USA ', 5110000 )
mem2 = ( 'Garry', 'JAPAN ', 1230000 )
mem3 = ( 'Smith', 'JAPAN ', 1230000 )
mem4 = ( 'Elizabeth' , 'France', 3313000 )
mem5 = ( 'Gromly', 'Korea', 135000 )

#어떤 숫자를 형식화하여 출력하는 방법

t1, t2, t3, t4= 11, 234, 5630, 381390232

print("그냥 찍기", t1, t2, t3, t4)

print(" format %+10d" % t1)
print(" format %+10d" % t2)
print(" format %10d" % t3)
print(" format %10d" % t4)
print("Tuple %5d %5d %5d %rd" %( t1, t2, t3, t4))


print(" format %-10d" % t1)
print(" format %-10d" % t2)
print(" format %-10d" % t3)
print(" format %-10d" % t4)


print("floating format %10.3f" % 23432.34281)
print("Today's stock price: %f" % 50.4625)
print("Today's stock price: %.2f" % 50.4625)
print("Change since yesterday: %+.2f" % 1.5)
print("padding %010d " % 34221)
print("padding %+010d " % 34221)
print("padding %+010d " % -547)


a= 23890.234
print("\n a값은 %10.5f" % a)

