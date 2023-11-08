
import time             #시간관련 함수를 쓰기 위해서 반드시 불러야 함.


print("time()=",    time.time())
print("clock()=",   time.clock())
ctimestring =  time.ctime()
ctimelist = ctimestring.split( )
print("ctime list()=",   ctimelist)
print("gmttime()=", time.gmtime())
print("\n기준시간대=", time.gmtime(0)) #1970년 GMT 0시 0분
print("localtime()=",time.localtime())

print("\n strftime() 사용해보기", end=' ')
print(time.strftime("%Y/%m/%d")) # p.866
t = time.strptime("2015/3/18", "%Y/%m/%d")
print("t=", t)
print(time.mktime(t))
print("측정한 시간대의 이름=", time.tzname[0])


print("수행시간 측정해보기")

start = time.clock()
s = 0
for x in range(10000) :
    for y in range(1000) :
        s += 1


end = time.clock( )
print("전체 걸린 시간(mili second)=", end-start)
