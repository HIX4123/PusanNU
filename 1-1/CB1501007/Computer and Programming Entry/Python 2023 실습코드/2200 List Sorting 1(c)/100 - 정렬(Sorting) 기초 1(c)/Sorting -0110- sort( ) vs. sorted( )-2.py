
# sorting( ): list 자료형의 method( ), 입력 매개변수 자체를 정렬함. 그 자체가 변함.
# sorted( ) : generic function. 뭐든 sort함.

slist  = ["summer", "time", "killer", "Who", "are", "you", "?"]

tlist = sorted( slist)

print("slist=", slist )
print("tlist=", tlist )


slist.sort()
print("slist.sort()=", slist)


