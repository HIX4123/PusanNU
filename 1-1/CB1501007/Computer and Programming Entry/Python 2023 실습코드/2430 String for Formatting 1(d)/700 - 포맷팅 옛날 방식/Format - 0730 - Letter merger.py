

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

lotte = [ mem1, mem2, mem4, mem3, mem5 ]
lotte.sort()
print("실험 1", lotte)

def mycmp(p1, p2) :
    return cmp(p1[1], p2[1])    #두번째 원소를 비교

#lotte.sort(mycmp)  #Python 3에서는 동작하지 않음, 2에서만 동작
#print("실험 2", lotte)