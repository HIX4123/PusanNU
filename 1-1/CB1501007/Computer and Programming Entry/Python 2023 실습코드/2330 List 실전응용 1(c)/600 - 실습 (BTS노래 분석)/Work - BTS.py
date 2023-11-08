

BTS =  open("BTS.txt", "r", encoding='cp949')

i=0
Lyric=[] # 가사 전체를 저장하는 list

for line in BTS:  #파일을 끝까지 읽고
    i += 1
    cline=line.split()
    #print( f'i={i:2},  {cline}')
    Lyric.append( cline )

BTS.close() # 열면 닫아야 한다.

THIS = "ah"
count = 0
for (i,zul) in enumerate(Lyric) :
##    print( f'i={i}, {zul}')
    for (j,w) in enumerate(zul) :
        if w == THIS :
            print(f' {i}-번째줄 {j}-번째 단어')
            count += 1


print(f' 단어{THIS}가 총 나타난 횟수={count}')
