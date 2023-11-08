# List의 기초에 대하여 배웁니다.
#
mylist = [6 , 0 ,1 , -2, 32, 57 ]

print( "mylist=",  mylist )


for w in mylist :
    print("element w=", w )


print("\n Enumerating \n")

for i,w in enumerate(mylist) :
    print("list[",i,"]=", w )