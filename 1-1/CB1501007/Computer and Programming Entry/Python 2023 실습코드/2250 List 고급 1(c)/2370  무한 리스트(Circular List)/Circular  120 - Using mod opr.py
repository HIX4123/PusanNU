

mlist  = list("computer")

myindex = 0
for i in range(30)  :
     print(f"i={i:3}, mlist= {mlist[myindex]}")
     myindex = (myindex+1)%len(mlist)