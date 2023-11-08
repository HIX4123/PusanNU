
#for loop은 어떤 리스트에서 원소를 하나씩 차례대로 꺼내는 작업을 한다.

import random

deco =  ["골때리는", "멍청한", "꿈꾸는", "멍때리는", "한심한" ]
entry = [ "달팽이", "너구리", "국회의원", "삵쾡이",  "양아치", "멋쟁이"]

rseed = eval(input("Type your birthday OOOO: "))
random.seed( rseed )
nick=[]

print("------ 2중 for loop 으로 별명만들기 ---")
for x in deco :
    for y in entry :
        newname = x + " " + y
#        print newname
        nick.append( newname )
    print()



yournick = random.choice( nick )
print(("당신의 별명은 = ", yournick))