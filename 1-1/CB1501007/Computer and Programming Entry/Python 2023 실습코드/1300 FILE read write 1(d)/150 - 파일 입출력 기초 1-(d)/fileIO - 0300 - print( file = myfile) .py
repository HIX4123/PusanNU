
# 우리가 지정한 파일로 쓸 경우에 사용하는 방법 file=this_out


print ("------------------------")
myfile = open("XXX.out", "w",encoding='cp949')
print ( "1. Start", file=myfile)
print ( "2. New BEG", file=myfile)
myfile.close();  #일단 닫으면 disk에 writing이 된다.

print ("------- 다시 XXX.out을 엽니다. ---------------")
myfile = open("XXX.out", "a")  # append, write
print ( "3. Start", file=myfile)
print ( "4. Start", file=myfile)
myfile.close();

print ("----------------------")
leftfile  = open("seoul.inp", "r", encoding='cp949')
rightfile = open("pusan.inp", "r", encoding='cp949')
wholeft   = leftfile.readline()
whoright  = rightfile.readline()
print (wholeft, whoright)

leftfile.close()
rightfile.close()