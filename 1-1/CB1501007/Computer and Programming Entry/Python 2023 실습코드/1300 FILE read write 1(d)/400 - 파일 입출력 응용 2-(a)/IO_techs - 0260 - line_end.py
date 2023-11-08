# 파일에서 한 줄을 읽고, 읽은 것을  그대로 쓰는 작업
# 아주 중요한, 기본 기능이므로 반드시 잘 익혀두어야 합니다.

myfile = open("EOF-test.inp", "r")   # r로 파일을 읽습니다. read
print("We begin with line-reading")
i=0

while True:                        # 계속 작업을 수행한다.
    line = myfile.readline()
#    if not line :         print "Oh!"
    if( line == '') :       # 마지막 줄의 검사. 반드시 뒷줄에 빈 return문자
        print("Ended")
        break   #While Loop을 빠져 나간다. break the while Loop
    else:
        print(i, "=>", (line))
        i=i+1



# 여기가 while loop의 끝입니다.


print("All experiment Done")