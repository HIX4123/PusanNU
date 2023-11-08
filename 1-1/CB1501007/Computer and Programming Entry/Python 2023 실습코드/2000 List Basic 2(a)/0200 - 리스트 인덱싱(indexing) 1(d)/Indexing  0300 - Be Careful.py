
la = [[0]*3]*4  # 곱하면 같은 id의 원소를 넣는다.
print("1. la=", la )

la[0][0]=1
print("2. la=", la )

sl= [1,2,3]
wl = sl*5
ql = [sl]*5
print("3. wl= ", wl)
print("4. ql= ", ql)

ql[0][-1]= 99
print("5. ql= ", ql)

# 어떻게 할 것인가 ?
bol = [ [0]*3 for i in range(4)]  # 생성을 3번 반복


print("6. bol= ", bol)
bol[0][-1]= 99
print("7. after bol = ", bol)

