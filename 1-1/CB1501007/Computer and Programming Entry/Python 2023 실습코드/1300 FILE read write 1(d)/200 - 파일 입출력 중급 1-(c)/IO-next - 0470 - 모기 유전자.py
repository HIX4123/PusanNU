# Problem Solving Class A
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 이름 - 팽길탄




fh =  open("mogi-dna-02.inp", "r")

i = 1

for line in fh:  # 한줄씩 가지고 온다.
    line = line.strip()
    if( "CGCGCG" in line ) :
        print(i, ":  ", line)

    i = i + 1 # 1증가


print("\n\n 총 라인 수는 = ", i )

fh.close()
