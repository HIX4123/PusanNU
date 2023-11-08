# a baseball player with hitting average p[0,1]
# Write a function to smipulate this p-hitter

import random
random.seed( 41234 )        # Random Number 시작점을 설정

def batting( p ) :
    if p > random.random( ) :
        return "H"  # hit
    else :
        return "O"  # out

streak=""           # 빈 스트링
for x in range(1,21) :
    result = batting(0.29)
    print(x, "-th -->", result)
    streak += result    # 문자를 붙임


print("최종 배팅 결과", streak)

# what is the streak after 130*3=400 batting ?
