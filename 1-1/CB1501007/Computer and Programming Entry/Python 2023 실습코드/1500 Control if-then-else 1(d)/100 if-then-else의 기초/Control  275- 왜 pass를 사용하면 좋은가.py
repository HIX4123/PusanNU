# 전체 모양으로 나중에 코드를 관리하게 편하게 만들어 준다.
# 이런 것을 consistent design이라고 한다.


a = 11
if a == 10:
    pass       # 뽀대를 갖추어 준다. 나중에 넣기에도 편함.
               # 나중에 여기에 그냥 적어 넣으면 된다.
else:
    print("a가 10이 아니라니!")

b = 11
if b == 10:     print('b는 10입니다.')
elif b == 11:   pass
else:
        print('b는 10도 11도 아닙니다.')

c = 20
if c == 10:
    print("c는 10 입니다.")
elif c == 20:
        print("c는 20 입니다.")
elif c == 30:
     print("c는 30 입니다.")
else:
    pass
