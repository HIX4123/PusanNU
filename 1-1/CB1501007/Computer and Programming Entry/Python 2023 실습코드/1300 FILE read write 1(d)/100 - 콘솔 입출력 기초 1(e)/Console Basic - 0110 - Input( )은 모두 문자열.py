# 입문 과제물 No.4 Triangle sample code
#           by Zoh


# 작업할 파일을 미리 열어 둡니다.

infile  = open("../hello.txt", "r")
sa, sb, sc = infile.readline().split()

a = int(sa)
b = int(sb)
c = int(sc)  #file pointer,  파일변수 a = 100

print("sa, sb, sc = ", sa, sb, sc)
print("sa + sb + sc = ", sa+sb+sc)
print("a + b + c = ", a+b+c)

infile.close()
