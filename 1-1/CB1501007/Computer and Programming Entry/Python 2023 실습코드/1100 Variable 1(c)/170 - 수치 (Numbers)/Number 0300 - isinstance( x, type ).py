L=[ 45, 6.7,  0.51e+10, -90, [34], 0b110110 ]


for w in L :
    if isinstance( w, int ) :       ## 변수 특성을 확인하는 방법
        print(f" { w }는 정수.  " )

    if isinstance( w, float ) :       ## 변수 특성을 확인하는 방법
        print(f" { w }는 실수.  " )

    if isinstance( w, list ) :       ## 변수 특성을 확인하는 방법
        print(f" { w }는 리스트(list).  " )
