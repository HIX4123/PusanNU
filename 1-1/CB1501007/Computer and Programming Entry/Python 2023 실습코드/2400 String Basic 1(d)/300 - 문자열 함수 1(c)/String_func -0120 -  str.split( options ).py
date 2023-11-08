
#-------------------------------------------------------------------------------
lines = '''first line is given
      second line
     third line
     The End of fileline. '''

myline = lines.splitlines() # 라인 단위로 분리
print("out1= ", myline)

s = 'one:two:three:four'
print("out2= ",s.split   (':', 2)) # 두 번만 분리 ['one', 'two', 'three:four']
print("out3= ",s.rsplit  (':', 1)) # 오른쪽부터 처리 ['one:two:three', 'four']


# 문자열을 정렬(align)하기, 줄 맞추기
u = 'spam and egg'
center  = u.center  (40)        # 전체 60문자의 가운데에 맞춤
left    = u.ljust   (40)        # 왼쪽에 맞춤
right   = u.rjust   (40)        # 오른쪽에 맞춤
fillcen = u.center  (40, '-')   # 공백 대신 '-' 문자로 채움

print("out5= ",u)
print("out6= ",center)
print("out7= ",left)
print("out8= ",right)
print("out9= ",fillcen)
