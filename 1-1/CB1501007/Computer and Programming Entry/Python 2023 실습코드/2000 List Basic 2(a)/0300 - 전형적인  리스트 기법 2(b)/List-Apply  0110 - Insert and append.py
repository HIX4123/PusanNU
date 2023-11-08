# List의 기초에 대하여 배웁니다.
#
mylist = [6 , 0 ,1 , -2, 32, 57 ]

print( "mylist=",  mylist )


mylist.insert(0, 100)
print( "mylist=",  mylist )

mylist.insert(-1, 333)
print( "mylist=",  mylist )

mylist.append( 444 )
print( "mylist=",  mylist )

mylist.insert( len(mylist), 999)
print( "mylist=",  mylist )