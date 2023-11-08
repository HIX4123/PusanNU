# List의 기초에 대하여 배웁니다. 교재 p.67
#
mylist = [6,0,1,2,2,7]
ertk = [ 9, 3, 4, 5, 0, 0, 8 ]
gilee = len(mylist)
print("리스트의 길이는", gilee, "입니다")

another = list(range(500))
print(another[45:50])

if ( 567 in another ) :
    print("있습니다")
else :
    print("없습니다")

another.append(999)
del another[0:100]
print("test 1=", another[0])
print("del이후 길이는 = ", len(another))
print("test 2=",another[-1])
print("리스트를 한번 뒤집어 봅니다")
another.reverse()
print("test 3=",another[0])
print("test 4=",another[-1])





