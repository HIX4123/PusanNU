# elif 활용하기

score = 87
grade = "w"


if    91 <= score : grade = "A"
elif  81 <= score : grade = "B"
elif  68 <= score : grade = "C"  # 68 < x =< 80
elif  45 <= score : grade = "D"
else : grade = "F"

print(score, "의 최종성적은 =", grade)


if 3 > 4 :
    print(4)
else :
    if ( 5 >= 67 ) :
        print(90)
    else :
        print( 788)

