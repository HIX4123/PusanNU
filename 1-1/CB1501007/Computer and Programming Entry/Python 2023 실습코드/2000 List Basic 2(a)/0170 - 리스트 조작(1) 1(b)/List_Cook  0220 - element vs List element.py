
x=100 ; y=200
lb=[x,y]   # 리스트에는 x의 값이 들어감. x 그 자체가 아니라.
print("Before lb=[x,y] ", lb)
print("Before x,y= ", x, y)
x= 900     # 따라서 x를 바꾸어도 전체 list lb는 변화가 없음
print("After x,y= ", x, y)
print("After lb=[x,y] ", lb)


print("\n 리스트를 넣을 경우 \n")
lx=[100]; ly=[200]
llxy=[ lx, ly]    # 리스트를 넣으면 원소 그 자체, 즉 리스트가 들어감.
print("Before llxy=[ lx, ly]  =", llxy)
lx.append(700)    # 위와 같이 원소 lx를 변화시킴
print("After llxy=[ lx, ly]  =", llxy)        #변화가 반영됨.