import os

fname = input("읽을 파일의 이름 : ")
if ( not os.path.isfile(fname) ) :
    print(f' 오류 FILE: {fname}이 없습니다. 종료 땡')
    exit(0)

f = open( fname , 'r')


mydata = f.readline( )
print(" mydata>>\n", mydata)
print(" 길이는 = ",  len(mydata))
print(" my data의 유형은 ",  type(mydata) )

multiline = mydata.split()
oneline = ''.join( multiline )
print("\n oneline = ", len(oneline),"\n>", oneline )

print("\n Who\n")
print(" Whom")

f.close()