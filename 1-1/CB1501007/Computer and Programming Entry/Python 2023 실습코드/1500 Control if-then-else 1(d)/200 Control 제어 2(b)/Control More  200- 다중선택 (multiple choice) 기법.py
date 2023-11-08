
Weight=[ 20,    35,    43,   53,   73,    83,   91,  95 ,  101 ]
Grade =['F',  'D0',  'D+', 'C0', 'C+',  'B0', 'B+', 'A0',  'A+']


for My in { 32, 55, 99, 12, 76, 54, 89, 91, 53} :
    i=0
    for w in Weight:
        if My <=  w :
            here = i
            break
        i += 1
    print(f"당신의 점수는 {My}, 등급은 {Grade[here]} ")



