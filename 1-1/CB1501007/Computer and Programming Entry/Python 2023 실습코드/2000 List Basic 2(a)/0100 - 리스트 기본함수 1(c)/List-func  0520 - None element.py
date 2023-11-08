# 빈 리스트 만들기

a= []

a.extend([None]*7)
print("1: a=", a)


a.extend([None]*3)
print("2: a=",a)

a.extend([None]*4)
print("3: a=",a)


a.append("Good")
print("4: a=",a)

a[3]="메롱"