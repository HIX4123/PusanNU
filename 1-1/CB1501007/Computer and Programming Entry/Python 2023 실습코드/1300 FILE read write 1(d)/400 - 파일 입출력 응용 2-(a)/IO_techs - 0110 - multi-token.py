# 파일에서 한 줄을 읽고, 읽은 것을  그대로 쓰는 작업
# 아주 중요한, 기본 기능이므로 반드시 잘 익혀두어야 합니다.

myfile = open("multi_token_line.txt", "r")  # r로 파일을 읽습니다. read

nsum = 0
tlist=[]
while( True ) :
    boy = myfile.readline()
    if boy == '' :  break
    tlist = boy.split()  #  끝 문자 제거, 반드시 필요함
    nlist = list(map( int, tlist))  # 각 원소를 mapping 함
    print(nlist, sum( nlist))
    a= sum(nlist)
    print("a=", a)
    nsum += a

print("NSUM = ", nsum)

myfile.close()